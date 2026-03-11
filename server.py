import hashlib
import hmac
import os
import time
import json
import socket
import struct
from collections import defaultdict
from pathlib import Path
from threading import Thread, Lock

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

load_dotenv()

ADMIN_PASSWORD_HASH: str = os.getenv("ADMIN_PASSWORD_HASH", "").lower()
PORT: int                = int(os.getenv("PORT", 3000))
NEWS_FILE = Path("news.json")
DOCS_FILE = Path("docs.json")

MC_HOST = os.getenv("MC_HOST", "blissfull.mc-server.net")
MC_PORT = int(os.getenv("MC_PORT", 25816))

app = Flask(__name__, static_folder=".")
CORS(app, origins=["*"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

RATE_WINDOW = 60
RATE_MAX    = 10
_rate_store: dict = defaultdict(lambda: {"count": 0, "reset_at": 0})
_status_cache = {"data": None, "updated_at": 0}
_status_lock  = Lock()

# ── Rate limit ────────────────────────────────────────────────────────────
def check_rate_limit(ip: str) -> bool:
    now   = time.time()
    entry = _rate_store[ip]
    if now > entry["reset_at"]:
        entry["count"]    = 0
        entry["reset_at"] = now + RATE_WINDOW
    entry["count"] += 1
    return entry["count"] <= RATE_MAX

# ── Minecraft ping ────────────────────────────────────────────────────────
def _write_varint(value: int) -> bytes:
    out = b""
    while True:
        b = value & 0x7F
        value >>= 7
        if value: b |= 0x80
        out += bytes([b])
        if not value: break
    return out

def _read_varint(stream) -> int:
    result = 0; shift = 0
    while True:
        b = stream.read(1)
        if not b: raise EOFError("Connection closed")
        byte = b[0]
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80): return result
        shift += 7
        if shift >= 35: raise ValueError("VarInt too large")

def ping_minecraft(host: str, port: int, timeout: float = 5.0) -> dict:
    addr_enc   = host.encode("utf-8")
    handshake  = (_write_varint(0x00) + _write_varint(762)
                  + _write_varint(len(addr_enc)) + addr_enc
                  + struct.pack(">H", port) + _write_varint(1))
    packet     = _write_varint(len(handshake)) + handshake
    status_req = _write_varint(1) + _write_varint(0x00)
    with socket.create_connection((host, port), timeout=timeout) as sock:
        sock.sendall(packet + status_req)
        stream = sock.makefile("rb")
        _read_varint(stream); _read_varint(stream)
        data = json.loads(stream.read(_read_varint(stream)).decode())
    return {
        "online":         True,
        "players_online": data.get("players", {}).get("online", 0),
        "players_max":    data.get("players", {}).get("max", 0),
        "version":        data.get("version", {}).get("name", "?"),
    }

def _refresh_status():
    while True:
        try: result = ping_minecraft(MC_HOST, MC_PORT)
        except: result = {"online": False, "players_online": 0, "players_max": 0, "version": "?"}
        with _status_lock:
            _status_cache["data"] = result
            _status_cache["updated_at"] = time.time()
        time.sleep(10)

Thread(target=_refresh_status, daemon=True).start()

# ── News helpers ──────────────────────────────────────────────────────────
DEFAULT_NEWS = []


def load_json(path: Path, default):
    if path.exists():
        try:
            content = path.read_text(encoding="utf-8").strip()
            if content:
                data = json.loads(content)
                if isinstance(data, list): return data
        except Exception as e:
            print(f"Warning loading {path}: {e}")
    save_json(path, default)
    return list(default)

def save_json(path: Path, data):
    try:
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(path)
    except Exception as e:
        print(f"Save error {path}: {e}")

def load_news(): return load_json(NEWS_FILE, DEFAULT_NEWS)
def save_news(d): save_json(NEWS_FILE, d)

# ── Docs helpers ──────────────────────────────────────────────────────────
DEFAULT_DOCS = [
    {
        "id": 1, "category": "Введение", "title": "Концепция сервера",
        "lead": "BlissFullReloaded — Vanilla+ сервер с элементами лёгкого RP, упором на PvE, кооперацию, экономику и постепенное исследование мира.",
        "body": "## Ключевые принципы\n\n- Мир расширяется постепенно — через общий банк XP всех игроков\n- Кооперация выгоднее одиночной игры\n- Социальные конфликты решаются через игровые органы власти\n- Администрация следит за читами, не вмешивается в социальные споры\n\n[box][b]Главная идея:[/b] каждая смерть имеет цену для всего сервера. Чем лучше выживает каждый — тем больше открытого мира для всех.[/box]\n\n[divider]Цифры сезона[/divider]\n\n[stats]\n[stat accent]∞[/stat][statlbl]Мир без конца[/statlbl]\n[stat purple]7[/stat][statlbl]Ролей власти[/statlbl]\n[stat gold]3x[/stat][statlbl]Макс. множитель XP[/statlbl]\n[stat green]100%[/stat][statlbl]Ванильное ядро[/statlbl]\n[/stats]",
        "order": 0
    },
    {
        "id": 2, "category": "Введение", "title": "Стартовый город",
        "lead": "В начале сезона все игроки появляются в одном месте — первом жилом поселении. Как оно будет называться и устроено — решают сами игроки.",
        "body": "## Инфраструктура\n\n[table]\n[th]Объект[/th][th]Управляет[/th][th]Функция[/th]\n[td]Мэрия[/td][td]Мэр[/td][td]Разрешения на строительство, управление городом[/td]\n[td]Суд[/td][td]Судья[/td][td]Разбор нарушений и конфликтов[/td]\n[td]Склады[/td][td]Мэр[/td][td]Городские ресурсы и резервы[/td]\n[td]Рынок[/td][td]Все[/td][td]Бочки-магазины, доска объявлений[/td]\n[td]Доска найма[/td][td]Все[/td][td]Заказы на добычу ресурсов и охоту на мобов[/td]\n[/table]\n\n[box warning][b]Плата за защиту:[/b] игрок платит не за участок, а за защиту которую обеспечивает город. Размер и условия устанавливает Мэр. В любой момент можно уйти и основать своё поселение.[/box]",
        "order": 1
    },
    {
        "id": 3, "category": "Мир", "title": "Всемирный барьер",
        "lead": "Центральная механика сервера. Радиус мирового барьера зависит от суммарного XP в общем банке всех игроков.",
        "body": "## Принцип работы\n\n[table striped]\n[th]Действие[/th][th]Эффект на банк[/th][th]Статус[/th]\n[td]Получение опыта[/td][td]XP → банк → барьер расширяется[/td][td][badge new]Активно[/badge][/td]\n[td]Смерть игрока[/td][td]Весь XP убитого вычитается из банка[/td][td][badge danger]Опасно[/badge][/td]\n[td]Зачарование / Переименование[/td][td]Трата XP — барьер НЕ уменьшается[/td][td][badge info]Нейтрально[/badge][/td]\n[td]BioMarket (органика)[/td][td]Органика → XP → банк напрямую[/td][td][badge new]Активно[/badge][/td]\n[td]Ночь и Нижний мир[/td][td]Множитель XP ×1.3[/td][td][badge new]Активно[/badge][/td]\n[td]Умышленный суицид[/td][td]Технический бан без предупреждения[/td][td][badge danger]БАН[/badge][/td]\n[/table]\n\n[cols2]\n[col]## Ограничения барьера\n\n- Минимальный размер — 250 блоков\n- Максимальный — не ограничен\n- Текущий XP и размер видны на скорборде справа\n[/col]\n[col]## Система эпох\n\n- [b]Камень / Медь[/b] — добыча не ниже -10 блоков\n- [b]Средние эпохи[/b] — открывается Нижний мир\n- [b]Поздние эпохи[/b] — открывается Энд\n[/col]\n[/cols2]\n\n[divider]Мировые рекорды — постоянные титулы[/divider]\n\n[table]\n[th]Достижение[/th][th]Награда[/th]\n[td]Первый скрафченный маяк[/td][td]Постоянный титул навсегда[/td]\n[td]Первое убийство Дракона Края[/td][td]Постоянный титул навсегда[/td]\n[/table]",
        "order": 2
    },
    {
        "id": 4, "category": "Мир", "title": "Система ивентов",
        "lead": "Ивенты запускаются автоматически. Активен только один одновременно — отображается на скорборде.",
        "body": "## Все ивенты\n\n[events]\n[ev]🟡 Золотая Лихорадка[/ev][evd]Опыт в банке умножается на ×3[/evd][evt]35 сек[/evt]\n[ev]🔴 Теневое Эмбарго[/ev][evd]XP перестаёт поступать в банк, но при смерти всё равно отнимается[/evd][evt]30 мин[/evt]\n[ev]💀 Жертвоприношение[/ev][evd]За каждую смерть банк получает +500 XP. Повторная смерть за сессию — без бонуса[/evd][evt]60 сек[/evt]\n[ev]👹 Охота на монстра[/ev][evd]Усиленный монстр рядом с рандомным игроком. Награда: 1000–2500 XP[/evd][evt]5 мин[/evt]\n[ev]🌀 Нестабильность[/ev][evd]Барьер «дышит» — сужается и расширяется поочерёдно. Только визуал[/evd][evt]60 сек[/evt]\n[ev]⚠️ Коллапс[/ev][evd]Барьер сужается 5 XP/сек. Нужно активно фармить чтобы остановить[/evd][evt]45 сек[/evt]\n[ev]🏘 Деревенский Рейд[/ev][evd]Запускается если игрок в деревне более 1 часа. Длится до победы[/evd][evt]До победы[/evt]\n[ev]❤️ Жертва сердцами[/ev][evd]Редкий ивент. Игроки жертвуют сердца добровольно — бонус получают все. По итогу таблица пожертвований[/evd][evt]Редкий[/evt]\n[/events]\n\n[box][b]Совет:[/b] во время Коллапса объединяйтесь — чем больше игроков фармит XP, тем быстрее стабилизируется барьер.[/box]",
        "order": 3
    },
    {
        "id": 5, "category": "Мир", "title": "Механики мира",
        "lead": "Уникальные правила и системы, которые делают выживание сложнее, интереснее и непредсказуемее.",
        "body": "## Динамическая сложность мобов\n\n[table striped]\n[th]Дистанция от спавна[/th][th]Множитель HP[/th][th]Пример[/th]\n[td]0 – 1 000 блоков[/td][td]×1.0 (ваниль)[/td][td]Зомби: 20 HP[/td]\n[td]1 000 – 3 000[/td][td]×1.25[/td][td]Зомби: 25 HP[/td]\n[td]3 000 – 7 000[/td][td]×1.6[/td][td]Зомби: 32 HP[/td]\n[td]10 000+[/td][td]×2.5+[/td][td]Паук: 200+ HP[/td]\n[/table]\n\n[cols2]\n[col]## Клаустрофобия\n\nДолгое пребывание под землёй вызывает дебаффы:\n\n- Тошнота и Слепота\n- Медлительность и Слабость\n\nПри входе на сервер — шанс уже иметь фобию. Нахождение рядом с [b]костром[/b] снимает фобию и останавливает спавн фантомов.\n[/col]\n[col]## Навигация\n\n- F3 отключён\n- Координаты — только с компасом в руке\n- При наведении на игрока — ник и лицензия\n- В Нижнем мире — ники искажаются\n[/col]\n[/cols2]\n\n[divider]Прочие механики[/divider]\n\n[table]\n[th]Механика[/th][th]Описание[/th][th]Статус[/th]\n[td]Замедленный рост[/td][td]Зерновые, ягоды и деревья растут значительно медленнее ванили[/td][td][badge new]Активно[/badge][/td]\n[td]Молнии и броня[/td][td]Гроза + медная броня = заметный шанс удара молнией[/td][td][badge new]Активно[/badge][/td]\n[td]Портал в Ад[/td][td]Минимальный размер рамки — 5×4 блока[/td][td][badge new]Активно[/badge][/td]\n[td]Скользкие поверхности[/td][td]На льду, слизи — шанс потери управления[/td][td][badge new]Активно[/badge][/td]\n[td]Незеритовая броня[/td][td]Полный комплект замедляет игрока. Снимается зачарованием Лёгкость[/td][td][badge new]Активно[/badge][/td]\n[td]BioMarket[/td][td]Органика (пшеница, морковь, лут с мобов) → XP в банк[/td][td][badge new]Активно[/badge][/td]\n[td]Улики на месте смерти[/td][td]После гибели выпадает предмет-улика с подсказкой о причине[/td][td][badge new]Активно[/badge][/td]\n[td]Крафт Ока Эндера[/td][td]Изменён: теперь требуется слеза гаста[/td][td][badge new]Активно[/badge][/td]\n[/table]",
        "order": 4
    },
    {
        "id": 6, "category": "Мир", "title": "Загадочные сундуки",
        "lead": "В данжах на случайных сундуках появляются магические барьеры. Чтобы открыть — нужна Пустая зачарованная книга.",
        "body": "[steps]\n[step]Крафт книги\nВозьмите обычную книгу и пузырёк с опытом. Объедините их на наковальне — получится Пустая зачарованная книга.[/step]\n[step]Найдите барьер\nВ данжах и структурах на случайных сундуках с ценным лутом появляется магический барьер.[/step]\n[step]Бросьте книгу\nДержа книгу в руке, бросьте её в барьер. Один из трёх исходов:[/step]\n[/steps]\n\n[zones]\n[zone safe]✨ Удача\nКнига превращается в зачарованную книгу с одним из уникальных новых зачарований сервера.\n[/zone]\n[zone danger]☠️ Ловушка\nКнига превращается в Неизвестную книгу. При открытии немедленно накладывает проклятие.\n[/zone]\n[zone warn]🔮 Третий исход\n[badge planned]Скоро[/badge] Готовится. Следите за обновлениями.\n[/zone]\n[/zones]\n\n[box warning][b]Осторожно:[/b] Неизвестную книгу можно передать другому игроку — он не будет знать что внутри.[/box]",
        "order": 5
    },
    {
        "id": 7, "category": "Снаряжение", "title": "Новые зачарования",
        "lead": "Уникальные зачарования, недоступные в стандартной игре. Получить через загадочные сундуки в данжах.",
        "body": "[divider]Защита и броня[/divider]\n\n[table striped]\n[th]Зачарование[/th][th]Тип[/th][th]Эффект[/th]\n[td]Нюхач[/td][td]Шлем[/td][td]Все игроки в радиусе 15 блоков подсвечиваются. Не работает с невидимостью[/td]\n[td]Плавник[/td][td]Нагрудник[/td][td]Ускоряет передвижение под водой[/td]\n[td]Лёгкость[/td][td]Броня (незер)[/td][td]Снимает штраф замедления в незеритовом сете. Достаточно одного фрагмента[/td]\n[td]Ветряной порыв[/td][td]Ботинки[/td][td]Увеличивает высоту прыжка[/td]\n[td]Дюноход[/td][td]Ботинки[/td][td]Ускоряет передвижение по песку[/td]\n[/table]\n\n[divider]Оружие и атака[/divider]\n\n[table striped]\n[th]Зачарование[/th][th]Тип[/th][th]Эффект[/th]\n[td]Импульс[/td][td]Меч, топор[/td][td]Шанс 1–5% — противник роняет оружие на землю[/td]\n[td]Цепная реакция[/td][td]Оружие[/td][td]Шанс 50% — все существа в радиусе 3 блоков получают 25% урона[/td]\n[td]Раскол[/td][td]Топор[/td][td]Урон идёт по броне противника — разрушает её в 1.5× быстрее[/td]\n[td]Кровотечение[/td][td]Топор, меч, лук и др.[/td][td]Шанс 10% — 2 сердца урона за 4 секунды[/td]\n[td]Вампиризм[/td][td]Оружие[/td][td]Шанс 3% — 20% текущего HP противника переходит к вам[/td]\n[td]Лассо (Кража)[/td][td]Удочка[/td][td]Шанс забрать предмет из рук противника в инвентарь[/td]\n[/table]\n\n[divider]Инструменты и особые[/divider]\n\n[table striped]\n[th]Зачарование[/th][th]Тип[/th][th]Эффект[/th]\n[td]Восстановление[/td][td]Мультитул, броня[/td][td]При поломке теряет зачарование, но восстанавливает 20% прочности[/td]\n[td]Вощение[/td][td]Медные инструменты и оружие[/td][td]Уровни I–V. Быстрее добывает, больше урона[/td]\n[td]Гарпун[/td][td]Трезубец[/td][td]34% шанс — при возврате трезубца в инвентарь залетает рыба[/td]\n[/table]",
        "order": 6
    },
    {
        "id": 8, "category": "Общество", "title": "Лицензии и роли",
        "lead": "Лицензии дают технические права и обязанности. Получить — через заявку и голосование в Discord.",
        "body": "[box warning][b]Ограничения:[/b] нельзя быть Мэром и Судьёй одновременно. Отсутствие >7 суток без уведомления — лицензия аннулируется. Передача аккаунта с лицензией — перманентный бан.[/box]\n\n## Все роли\n\n[table striped]\n[th]Роль[/th][th]Технические права[/th][th]Обязанности[/th][th]Лимит[/th]\n[td]Мэр[/td][td]Разрешения на стройку в спецзонах[/td][td]Дороги, развитие города, назначение глав[/td][td]1 человек[/td]\n[td]Судья[/td][td]Префикс [Преступник], штрафы[/td][td]Вердикты только по логам Следователя[/td][td]1 человек[/td]\n[td]Следователь[/td][td]`/co i`, `/co near`[/td][td]Сбор улик, нейтралитет[/td][td]1-2 человека[/td]\n[td]Охрана порядка[/td][td]`/freeze`, `/unfreeze`[/td][td]Задержание до суда[/td][td]До 3 человек[/td]\n[td]Адвокат[/td][td]Доступ в зону задержания[/td][td]Помощь игрокам, аудит договоров[/td][td]Без лимита[/td]\n[td]Строитель[/td][td]`/hat`, `/ec`[/td][td]Заказы Мэра, реставрация построек[/td][td]Без лимита[/td]\n[td]Ивент-менеджер[/td][td]`/broadcast`[/td][td]Минимум 1 событие в 2 недели[/td][td]1-2 человека[/td]\n[td]Алхимик[/td][td]Подкласс: Пивовар или Бармен[/td][td]Варка зелий и алкоголя, управление баром[/td][td]Без лимита[/td]\n[/table]\n\n[steps]\n[step]Подать заявку в Discord\nОписать кандидатуру, опыт на сервере и мотивацию в специальном канале.[/step]\n[step]Голосование игроков\nВ течение 48 часов действующие игроки голосуют за кандидата.[/step]\n[step]Утверждение Мэром\nПри положительном голосовании Мэр выдаёт лицензию.[/step]\n[/steps]",
        "order": 7
    },
    {
        "id": 9, "category": "Общество", "title": "Экономика и торговля",
        "lead": "Живая экономика между игроками — умные бочки-магазины, заказы через доску и кланы.",
        "body": "## Умные бочки (SmartBarrel)\n\n[table striped]\n[th]Тип[/th][th]Товаров[/th][th]Склад[/th][th]Описание[/th]\n[td]Магазин[/td][td]1[/td][td]18 слотов[/td][td]Один товар, фиксированная цена. ЛКМ ×1, ПКМ ×16, Shift ×64[/td]\n[td]Бар[/td][td]Несколько[/td][td]54 слота[/td][td]Разные напитки, у каждого своя цена[/td]\n[td]Уникальный[/td][td]Несколько[/td][td]54 слота[/td][td]Как бар, но для любых предметов[/td]\n[/table]\n\n[cols2]\n[col]## Доска объявлений\n\nИгроки размещают заказы на добычу ресурсов, охоту на мобов и другие услуги. Другие берут заказы и выполняют за вознаграждение.\n\nТакже поддерживает [b]анонимные доносы[/b] — имя отправителя не раскрывается.\n[/col]\n[col]## Кланы\n\n- Группа от 3 человек выбирает представителя\n- Право на коллективные иски в суд\n- Переговоры ведутся официально\n[/col]\n[/cols2]\n\n[box][b]Оффлайн-торговля:[/b] выставьте товар в бочке — другой купит пока вы офлайн. Выручка накапливается в кассе бочки.[/box]",
        "order": 8
    },
    {
        "id": 10, "category": "Справочник", "title": "Команды игрока",
        "lead": "Полный справочник доступных команд для всех игроков.",
        "body": "## Регистрация и вход\n\n[table]\n[th]Команда[/th][th]Описание[/th]\n[td]/register[/td][td]Регистрация при первом входе[/td]\n[td]/login, /l[/td][td]Авторизация при каждом входе[/td]\n[td]/changepassword[/td][td]Смена пароля[/td]\n[/table]\n\n## Чат\n\n[table striped]\n[th]Команда[/th][th]Описание[/th]\n[td]/msg <ник> <текст>[/td][td]Личное сообщение[/td]\n[td]/r <текст>[/td][td]Ответить последнему собеседнику[/td]\n[td]/ignore <ник>[/td][td]Заблокировать игрока[/td]\n[td]/unignore <ник>[/td][td]Снять блокировку[/td]\n[td]/me <текст>[/td][td]Ролевое действие от третьего лица[/td]\n[/table]\n\n## Анимации и быт\n\n[table]\n[th]Команда[/th][th]Действие[/th]\n[td]/sit[/td][td]Сесть (или ПКМ по ступеньке)[/td]\n[td]/lay[/td][td]Лечь на спину[/td]\n[td]/crawl[/td][td]Ползти по-пластунски[/td]\n[td]/bellyflop[/td][td]Лечь на животик[/td]\n[td]/Sleeper[/td][td]Пропустить ночь голосованием[/td]\n[/table]\n\n## Сундуки\n\n[table]\n[th]Команда[/th][th]Описание[/th]\n[td]/lock[/td][td]Заблокировать свой сундук[/td]\n[td]/unlock[/td][td]Открыть для общего доступа[/td]\n[td]/trust <ник>[/td][td]Добавить доверенного игрока[/td]\n[/table]\n\n## Скины и визуал\n\n[table striped]\n[th]Команда[/th][th]Описание[/th]\n[td]/skin set <ник>[/td][td]Скин другого игрока[/td]\n[td]/skin url <ссылка>[/td][td]Скин по URL[/td]\n[td]/skin clear[/td][td]Вернуть стандартный скин[/td]\n[td]/skin update[/td][td]Обновить скин с Mojang[/td]\n[td]/hat[/td][td]Надеть предмет на голову [badge planned]Строители[/badge][/td]\n[td]/ec, /enderchest[/td][td]Карманный эндер-сундук [badge planned]Строители[/badge][/td]\n[td]/imageframe create <имя> <url> <ш> <в>[/td][td]Разместить GIF или картинку. Нужны карты в инвентаре[/td]\n[/table]\n\n## Алкоголь (Brewery)\n\n[table]\n[th]Команда[/th][th]Описание[/th]\n[td]/brew help[/td][td]Список команд плагина[/td]\n[td]/brew info[/td][td]Информация о напитке в руке[/td]\n[td]/brew wakeup[/td][td]Выйти из опьянения[/td]\n[td]/brew drain[/td][td]Слить жидкость из бочки[/td]\n[td]/brew create[/td][td]Создать бочку для брожения[/td]\n[/table]",
        "order": 9
    },
    {
        "id": 11, "category": "Справочник", "title": "Правила сервера",
        "lead": "Незнание правил не освобождает от ответственности. Заходя на сервер — вы соглашаетесь с ними.",
        "body": "[box danger][b]Важно:[/b] некоторые нарушения влекут моментальный бан без предупреждений.[/box]\n\n## Поведение в сообществе\n\n- Запрещены оскорбления, пропаганда насилия, экстремизм, межнациональная рознь\n- Спам, флуд, злоупотребление CAPS — запрещены\n- Никнейм, скин, аватар Discord — без оскорблений и неприемлемого контента\n\n## Технические нарушения → Административный бан\n\n[table]\n[th]Нарушение[/th][th]Наказание[/th]\n[td]Читы: X-Ray, KillAura, Fly и любое ПО с преимуществом[/td][td][badge danger]Мгновенный бан[/badge][/td]\n[td]Дюп предметов, эксплойты барьера[/td][td][badge danger]Мгновенный бан[/badge][/td]\n[td]Лаг-машины и намеренная нагрузка сервера[/td][td][badge danger]Мгновенный бан[/badge][/td]\n[td]Умышленный суицид для сужения барьера[/td][td][badge danger]Мгновенный бан[/badge][/td]\n[/table]\n\n## Игровые нарушения → Судебный разбор\n\n[zones]\n[zone danger]⚠️ Нарушения в городе\n- Гриферство — уничтожение чужих построек\n- Кража из защищённых контейнеров\n- Незаконное ПВП — убийство без согласия\n[/zone]\n[zone warn]📋 Порядок наказаний\n- 1-е нарушение: Предупреждение\n- 2-е: Мут, кик или ограничение\n- 3-е и далее: Временный или перм. бан\n[/zone]\n[/zones]\n\n## Строительство\n\n- Приват: метки по периметру + табличка с ником\n- Запрещены столбы 1×1, коробки из земли, парящие блоки\n- Стройка в спецзонах города — только с разрешения Мэра",
        "order": 10
    },
]


def load_docs(): return load_json(DOCS_FILE, DEFAULT_DOCS)
def save_docs(d): save_json(DOCS_FILE, d)

# ── Routes ────────────────────────────────────────────────────────────────
@app.get("/")
def index(): return send_from_directory(".", "index.html")

@app.post("/api/reset")
def reset_data():
    """Сброс docs.json и news.json к дефолтным значениям (требует пароль)"""
    data = request.get_json(silent=True) or {}
    password = data.get("password", "")
    if not password or not hmac.compare_digest(hashlib.sha256(password.encode()).hexdigest(), ADMIN_PASSWORD_HASH):
        return jsonify({"ok": False, "error": "Unauthorized"}), 401
    save_json(DOCS_FILE, DEFAULT_DOCS)
    save_json(NEWS_FILE, DEFAULT_NEWS)
    return jsonify({"ok": True, "message": "Данные сброшены к дефолтным"})

@app.get("/api/status")
def get_status():
    with _status_lock:
        data = _status_cache["data"]; updated_at = _status_cache["updated_at"]
    if data is None:
        return jsonify({"online": False, "players_online": 0, "players_max": 0, "version": "?", "updated_at": 0})
    return jsonify({**data, "updated_at": updated_at})

@app.post("/auth")
def auth():
    ip = request.headers.get("x-forwarded-for", request.remote_addr).split(",")[0].strip()
    if not check_rate_limit(ip):
        return jsonify({"ok": False, "error": "Too many requests"}), 429
    data = request.get_json(silent=True) or {}
    password = data.get("password", "")
    if not password: return jsonify({"ok": False}), 400
    ok = hmac.compare_digest(hashlib.sha256(password.encode()).hexdigest(), ADMIN_PASSWORD_HASH)
    return jsonify({"ok": ok}), 200 if ok else 401

# ── News API ──────────────────────────────────────────────────────────────
@app.get("/api/news")
def get_news(): return jsonify(load_news())

@app.post("/api/news")
def add_news():
    data = request.get_json(silent=True) or {}
    if not data.get("title") or not data.get("text"):
        return jsonify({"ok": False, "error": "title and text required"}), 400
    news = load_news()
    item = {"id": int(time.time()*1000), "type": data.get("type","info"),
            "typeLabel": data.get("typeLabel","Инфо"), "date": data.get("date",""),
            "title": data["title"], "text": data["text"], "tags": data.get("tags",[])}
    news.insert(0, item); save_news(news)
    return jsonify({"ok": True, "item": item})

@app.put("/api/news/<int:news_id>")
def edit_news(news_id):
    data = request.get_json(silent=True) or {}
    news = load_news()
    for i, item in enumerate(news):
        if item["id"] == news_id:
            news[i] = {**item, **{k: data[k] for k in ["type","typeLabel","date","title","text","tags"] if k in data}}
            save_news(news); return jsonify({"ok": True, "item": news[i]})
    return jsonify({"ok": False, "error": "not found"}), 404

@app.delete("/api/news/<int:news_id>")
def delete_news(news_id):
    news = load_news()
    new_news = [n for n in news if n["id"] != news_id]
    if len(new_news) == len(news): return jsonify({"ok": False, "error": "not found"}), 404
    save_news(new_news); return jsonify({"ok": True})

# ── Docs API ──────────────────────────────────────────────────────────────
@app.get("/api/docs")
def get_docs():
    docs = load_docs()
    docs.sort(key=lambda d: d.get("order", 0))
    return jsonify(docs)

@app.post("/api/docs")
def add_doc():
    data = request.get_json(silent=True) or {}
    if not data.get("title"):
        return jsonify({"ok": False, "error": "title required"}), 400
    docs = load_docs()
    max_order = max((d.get("order", 0) for d in docs), default=-1)
    item = {
        "id":       int(time.time()*1000),
        "category": data.get("category", "Общее"),
        "title":    data["title"],
        "lead":     data.get("lead", ""),
        "body":     data.get("body", ""),
        "order":    max_order + 1,
    }
    docs.append(item); save_docs(docs)
    return jsonify({"ok": True, "item": item})

@app.put("/api/docs/<int:doc_id>")
def edit_doc(doc_id):
    data = request.get_json(silent=True) or {}
    docs = load_docs()
    for i, item in enumerate(docs):
        if item["id"] == doc_id:
            for k in ["category", "title", "lead", "body"]:
                if k in data: docs[i][k] = data[k]
            save_docs(docs); return jsonify({"ok": True, "item": docs[i]})
    return jsonify({"ok": False, "error": "not found"}), 404

@app.delete("/api/docs/<int:doc_id>")
def delete_doc(doc_id):
    docs = load_docs()
    new_docs = [d for d in docs if d["id"] != doc_id]
    if len(new_docs) == len(docs): return jsonify({"ok": False, "error": "not found"}), 404
    save_docs(new_docs); return jsonify({"ok": True})

@app.post("/api/docs/<int:doc_id>/move")
def move_doc(doc_id):
    data = request.get_json(silent=True) or {}
    direction = int(data.get("direction", 1))  # -1 = up, 1 = down
    docs = load_docs()
    docs.sort(key=lambda d: d.get("order", 0))
    idx = next((i for i, d in enumerate(docs) if d["id"] == doc_id), None)
    if idx is None: return jsonify({"ok": False}), 404
    swap = idx + direction
    if 0 <= swap < len(docs):
        docs[idx]["order"], docs[swap]["order"] = docs[swap]["order"], docs[idx]["order"]
        save_docs(docs)
    return jsonify({"ok": True})

@app.get("/health")
def health(): return jsonify({"status": "ok"})

if __name__ == "__main__":
    if not ADMIN_PASSWORD_HASH:
        print("⚠️  ВНИМАНИЕ: ADMIN_PASSWORD_HASH не задан в .env!")
    else:
        print("✅ Auth ready")
    print(f"🔍 Пингуем {MC_HOST}:{MC_PORT} каждые 10 сек...")
    app.run(host="0.0.0.0", port=PORT)
