import hashlib
import hmac
import os
import time
import json
from collections import defaultdict
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

load_dotenv()

ADMIN_PASSWORD_HASH: str = os.getenv("ADMIN_PASSWORD_HASH", "").lower()
ALLOWED_ORIGIN: str      = os.getenv("ALLOWED_ORIGIN", "*")
PORT: int                = int(os.getenv("PORT", 3000))
NEWS_FILE = Path("news.json")

app = Flask(__name__, static_folder=".")
CORS(app, origins=["*"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

RATE_WINDOW = 60
RATE_MAX    = 10
_rate_store: dict = defaultdict(lambda: {"count": 0, "reset_at": 0})

def check_rate_limit(ip: str) -> bool:
    now   = time.time()
    entry = _rate_store[ip]
    if now > entry["reset_at"]:
        entry["count"]    = 0
        entry["reset_at"] = now + RATE_WINDOW
    entry["count"] += 1
    return entry["count"] <= RATE_MAX

DEFAULT_NEWS = [
    {"id":1,"type":"update","typeLabel":"Обновление","date":"22.02.2026","title":"SmartBarrel v1.7 — Уникальный режим магазина","text":"Добавлен режим «Уникальные предметы» для бочек-магазинов. Теперь можно продавать разные предметы с индивидуальными ценами в одной бочке — как в баре. Также исправлены дюп-баги и расширен склад бара до 54 слотов.","tags":["SmartBarrel","Экономика","Фикс"]},
    {"id":2,"type":"update","typeLabel":"Обновление","date":"22.02.2026","title":"EternalBorder v2.0 — Стабильный релиз","text":"Полный рефакторинг плагина барьера. Модульная архитектура, исправлены утечки памяти, добавлена интеграция с TradeExperience.","tags":["EternalBorder","Барьер","Стабильность"]},
    {"id":3,"type":"announce","typeLabel":"Анонс","date":"23.02.2026","title":"Столица и система ПВП — в разработке","text":"Официально подтверждена новая концепция: единый стартовый город (Столица) с РП-постройками, платной защитой и доской найма.","tags":["Столица","ПВП","Анонс"]},
    {"id":4,"type":"event","typeLabel":"Событие","date":"19.02.2026","title":"Войны фракций — механика подтверждена","text":"Система городов и фракций официально войдёт в сервер при росте онлайна.","tags":["Фракции","Войны","Планы"]}
]

def load_news():
    if NEWS_FILE.exists():
        try:
            return json.loads(NEWS_FILE.read_text(encoding="utf-8"))
        except:
            pass
    return DEFAULT_NEWS

def save_news(news):
    NEWS_FILE.write_text(json.dumps(news, ensure_ascii=False, indent=2), encoding="utf-8")

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

@app.post("/auth")
def auth():
    ip = request.headers.get("x-forwarded-for", request.remote_addr).split(",")[0].strip()
    if not check_rate_limit(ip):
        return jsonify({"ok": False, "error": "Too many requests"}), 429
    data = request.get_json(silent=True) or {}
    password = data.get("password", "")
    if not password:
        return jsonify({"ok": False}), 400
    incoming_hash = hashlib.sha256(password.encode()).hexdigest()
    ok = hmac.compare_digest(incoming_hash, ADMIN_PASSWORD_HASH)
    return jsonify({"ok": ok}), 200 if ok else 401

@app.get("/api/news")
def get_news():
    return jsonify(load_news())

@app.post("/api/news")
def add_news():
    data = request.get_json(silent=True) or {}
    if not data.get("title") or not data.get("text"):
        return jsonify({"ok": False, "error": "title and text required"}), 400
    news = load_news()
    new_item = {
        "id": int(time.time() * 1000),
        "type": data.get("type", "info"),
        "typeLabel": data.get("typeLabel", "Инфо"),
        "date": data.get("date", ""),
        "title": data.get("title", ""),
        "text": data.get("text", ""),
        "tags": data.get("tags", [])
    }
    news.insert(0, new_item)
    save_news(news)
    return jsonify({"ok": True, "item": new_item})

@app.put("/api/news/<int:news_id>")
def edit_news(news_id):
    data = request.get_json(silent=True) or {}
    news = load_news()
    for i, item in enumerate(news):
        if item["id"] == news_id:
            news[i] = {**item, **{k: data[k] for k in ["type","typeLabel","date","title","text","tags"] if k in data}}
            save_news(news)
            return jsonify({"ok": True, "item": news[i]})
    return jsonify({"ok": False, "error": "not found"}), 404

@app.delete("/api/news/<int:news_id>")
def delete_news(news_id):
    news = load_news()
    new_news = [n for n in news if n["id"] != news_id]
    if len(new_news) == len(news):
        return jsonify({"ok": False, "error": "not found"}), 404
    save_news(new_news)
    return jsonify({"ok": True})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    if not ADMIN_PASSWORD_HASH:
        print("⚠️  ВНИМАНИЕ: ADMIN_PASSWORD_HASH не задан в .env!")
    else:
        print("✅ Auth server ready")
    app.run(host="0.0.0.0", port=PORT)
