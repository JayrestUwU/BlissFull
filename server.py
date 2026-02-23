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
DEFAULT_NEWS = [
    {"id":1,"type":"update","typeLabel":"Обновление","date":"22.02.2026","title":"SmartBarrel v1.7","text":"Добавлен режим «Уникальные предметы» для бочек-магазинов.","tags":["SmartBarrel","Экономика"]},
    {"id":2,"type":"update","typeLabel":"Обновление","date":"22.02.2026","title":"EternalBorder v2.0","text":"Полный рефакторинг плагина барьера.","tags":["EternalBorder","Барьер"]},
    {"id":3,"type":"announce","typeLabel":"Анонс","date":"23.02.2026","title":"Столица и система ПВП — в разработке","text":"Официально подтверждена новая концепция.","tags":["Столица","ПВП"]},
    {"id":4,"type":"event","typeLabel":"Событие","date":"19.02.2026","title":"Войны фракций — механика подтверждена","text":"Система городов и фракций.","tags":["Фракции"]}
]

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
        "body": "## Ключевые принципы\n- Один стартовый город (Столица) — точка входа и центр жизни сервера\n- Мир расширяется постепенно — через общий банк XP всех игроков\n- В Столице — мир и закон. За её пределами — дикие земли, полное ПВП\n- Кооперация выгоднее одиночной игры\n- Социальные конфликты решаются через игровые органы власти\n- Администрация следит за читами, не вмешивается в социальные споры\n\nГлавная идея: каждая смерть имеет цену для всего сервера. Чем лучше выживает каждый — тем больше открытого мира для всех.",
        "order": 0
    },
    {
        "id": 2, "category": "Мир", "title": "Столица",
        "lead": "Единственный город на старте сезона. Центр торговли, власти и безопасности. Все новые игроки появляются здесь.",
        "body": "## Инфраструктура\n- Мэрия — управление городом, выдача разрешений, тендеры\n- Суд — разбор нарушений и конфликтов\n- Склады — городские ресурсы под управлением Мэра\n- Рынок — основная торговая площадь\n- Доска найма — заказы на добычу ресурсов и охоту\n\n## Плата за защиту\n- Игрок платит не за участок, а за защиту которую обеспечивает Столица\n- Размер и условия оплаты устанавливает Мэр\n- Игрок в любой момент может покинуть Столицу",
        "order": 1
    },
    {
        "id": 3, "category": "Мир", "title": "ПВП и дикие земли",
        "lead": "За пределами Столицы действуют законы дикого мира. Полное ПВП без ограничений.",
        "body": "## Зоны\n- Столица — мирная зона, ПВП запрещено, базы защищены\n- Дикие земли — полное ПВП, убийство и рейд баз разрешены\n- ПВП арены — добровольные схватки внутри Столицы\n\n## Правила диких земель\n- Убийство игроков — разрешено без предупреждения\n- Рейд базы — разрешён: можно ломать постройки, красть ресурсы\n- Трофеи убитого игрока достаются победителю",
        "order": 2
    },
    {
        "id": 4, "category": "Мир", "title": "Всемирный барьер",
        "lead": "Центральная механика сервера. Радиус мирового барьера зависит от суммарного XP в общем банке.",
        "body": "## Принцип работы\n- Получение опыта → XP записывается в общий банк → барьер расширяется\n- Смерть игрока → весь накопленный опыт отнимается из банка → барьер сужается\n- Зачарование / Переименование → трата XP, барьер НЕ уменьшается\n\n## Система Эпох\n- Начальная эпоха — только Верхний мир\n- Средние эпохи — открывается Ад\n- Поздние эпохи — открывается Энд\n\nВажно: умышленный суицид с целью сужения барьера — технический бан без предупреждения.",
        "order": 3
    },
    {
        "id": 5, "category": "Мир", "title": "Система ивентов",
        "lead": "Ивенты запускаются автоматически и влияют на работу барьера и игровой процесс.",
        "body": "## Все ивенты\n- Золотая Лихорадка — опыт в банке умножается на 3х (35 сек)\n- Теневое Эмбарго — XP перестаёт поступать в банк, но при смерти отнимается (30 мин)\n- Жертвоприношение — за каждую смерть банк получает +500 XP (60 сек)\n- Охота на монстра — усиленный монстр рядом с игроком. Награда: 1000–2500 XP\n- Нестабильность — барьер «дышит», сужается и расширяется поочерёдно\n- Коллапс — барьер сужается 5 XP/сек, нужно активно фармить\n- Деревенский Рейд — запускается если игрок в деревне более 1 часа",
        "order": 4
    },
    {
        "id": 6, "category": "Общество", "title": "Лицензии и роли",
        "lead": "Лицензии дают технические права и обязанности. Получить — через заявку и голосование в Discord.",
        "body": "## Роли\n- Мэр — разрешения на стройку в спецзонах, тендеры, развитие Столицы\n- Судья — префикс [Преступник], штрафы, вердикты по логам Следователя\n- Следователь — /co i, /co near, сбор улик, нейтралитет\n- Охрана порядка — /freeze, /unfreeze, задержание до суда\n- Адвокат — доступ в зону задержания, помощь игрокам\n- Строитель — /hat, /ec, заказы Мэра, реставрация\n- Ивент-менеджер — /broadcast, минимум 1 событие в 2 недели\n\nОграничения: нельзя быть Мэром и Судьёй одновременно. Отсутствие более 7 суток без уведомления — лицензия аннулируется.",
        "order": 5
    },
    {
        "id": 7, "category": "Общество", "title": "Экономика и торговля",
        "lead": "Живая экономика между игроками. Умные бочки-магазины, онлайн-торги, государственные тендеры.",
        "body": "## Умные бочки (SmartBarrel)\n- Магазин — один товар, фиксированная цена, склад 18 слотов\n- Бар — разные напитки, у каждого своя цена, склад 54 слота\n- Уникальный — как бар, но для любых предметов\n\n## Онлайн-торги\n- Игрок размещает объявление на доске в Столице\n- Покупатель связывается в чате и договаривается\n- Обмен лично — встречаются и передают предметы напрямую\n- Споры при мошенничестве — разбирает Судья\n\n## Тендеры\n- Тендер — официальный заказ от Мэра, условия фиксируются в Discord\n- Клан даёт право на коллективные иски и участие в тендерах",
        "order": 6
    },
    {
        "id": 8, "category": "Справочник", "title": "Команды игрока",
        "lead": "Полный справочник доступных команд.",
        "body": "## Регистрация\n- /register — регистрация при первом входе\n- /login, /l — авторизация при каждом входе\n- /changepassword — смена пароля\n\n## Чат\n- /msg <ник> <текст> — личное сообщение\n- /r <текст> — ответить последнему собеседнику\n- /ignore <ник> — заблокировать игрока\n- /me <текст> — ролевое действие\n\n## Быт\n- /sit — сесть\n- /lay — лечь\n- /crawl — ползти\n\n## Сундуки\n- /lock — заблокировать свой сундук\n- /unlock — открыть для общего доступа\n- /trust <ник> — добавить доверенного игрока\n\n## Скины\n- /skin set <ник> — скин другого игрока\n- /skin url <ссылка> — скин по ссылке\n- /skin clear — стандартный скин",
        "order": 7
    },
    {
        "id": 9, "category": "Справочник", "title": "Правила сервера",
        "lead": "Незнание правил не освобождает от ответственности. Заходя на сервер — вы соглашаетесь с ними.",
        "body": "## Поведение\n- Запрещены оскорбления, пропаганда насилия, экстремизм\n- Спам, флуд, злоупотребление CAPS — запрещены\n- Никнейм, скин, аватар Discord — без оскорблений\n\n## Технические нарушения → Административный бан\n- Читы: X-Ray, KillAura, Fly и любое ПО с преимуществом\n- Дюп предметов, эксплойты барьера, лаг-машины\n- Умышленный суицид для сужения барьера\n\n## Игровые нарушения → Суд\n- Гриферство — уничтожение чужих построек в зоне Столицы\n- Кража — из защищённых контейнеров в Столице\n- Незаконное PvP — убийство без согласия внутри Столицы\n\n## Наказания\n- 1-е нарушение — предупреждение\n- 2-е — мут, кик или ограничение доступа\n- 3-е и далее — временный или постоянный бан\n- Серьёзные нарушения — моментальный бан",
        "order": 8
    },
]

def load_docs(): return load_json(DOCS_FILE, DEFAULT_DOCS)
def save_docs(d): save_json(DOCS_FILE, d)

# ── Routes ────────────────────────────────────────────────────────────────
@app.get("/")
def index(): return send_from_directory(".", "index.html")

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
