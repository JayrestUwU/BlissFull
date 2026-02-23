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
ALLOWED_ORIGIN: str      = os.getenv("ALLOWED_ORIGIN", "*")
PORT: int                = int(os.getenv("PORT", 3000))
NEWS_FILE = Path("news.json")

MC_HOST = os.getenv("MC_HOST", "blissfull.mc-server.net")
MC_PORT = int(os.getenv("MC_PORT", 25816))

app = Flask(__name__, static_folder=".")
CORS(app, origins=["*"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

RATE_WINDOW = 60
RATE_MAX    = 10
_rate_store: dict = defaultdict(lambda: {"count": 0, "reset_at": 0})

_status_cache = {"data": None, "updated_at": 0}
_status_lock  = Lock()

def check_rate_limit(ip: str) -> bool:
    now   = time.time()
    entry = _rate_store[ip]
    if now > entry["reset_at"]:
        entry["count"]    = 0
        entry["reset_at"] = now + RATE_WINDOW
    entry["count"] += 1
    return entry["count"] <= RATE_MAX

def _write_varint(value: int) -> bytes:
    out = b""
    while True:
        b = value & 0x7F
        value >>= 7
        if value:
            b |= 0x80
        out += bytes([b])
        if not value:
            break
    return out

def _read_varint(stream) -> int:
    result = 0
    shift  = 0
    while True:
        b = stream.read(1)
        if not b:
            raise EOFError("Connection closed")
        byte = b[0]
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            return result
        shift += 7
        if shift >= 35:
            raise ValueError("VarInt too large")

def ping_minecraft(host: str, port: int, timeout: float = 5.0) -> dict:
    protocol_version = _write_varint(762)
    server_address   = host.encode("utf-8")
    server_address   = _write_varint(len(server_address)) + server_address
    server_port      = struct.pack(">H", port)
    next_state       = _write_varint(1)

    handshake_data = (
        _write_varint(0x00) +
        protocol_version +
        server_address +
        server_port +
        next_state
    )
    handshake_packet = _write_varint(len(handshake_data)) + handshake_data
    status_request   = _write_varint(1) + _write_varint(0x00)

    with socket.create_connection((host, port), timeout=timeout) as sock:
        sock.sendall(handshake_packet + status_request)
        stream = sock.makefile("rb")
        _read_varint(stream)   # length
        _read_varint(stream)   # packet id
        json_length = _read_varint(stream)
        json_data   = stream.read(json_length)

    data = json.loads(json_data.decode("utf-8"))
    return {
        "online":         True,
        "players_online": data.get("players", {}).get("online", 0),
        "players_max":    data.get("players", {}).get("max", 0),
        "version":        data.get("version", {}).get("name", "?"),
    }

def _refresh_status():
    while True:
        try:
            result = ping_minecraft(MC_HOST, MC_PORT)
        except Exception as e:
            result = {"online": False, "players_online": 0, "players_max": 0, "version": "?"}
        with _status_lock:
            _status_cache["data"]       = result
            _status_cache["updated_at"] = time.time()
        time.sleep(10)

Thread(target=_refresh_status, daemon=True).start()

DEFAULT_NEWS = [
    {"id":1,"type":"update","typeLabel":"Обновление","date":"22.02.2026","title":"SmartBarrel v1.7 — Уникальный режим магазина","text":"Добавлен режим «Уникальные предметы» для бочек-магазинов.","tags":["SmartBarrel","Экономика","Фикс"]},
    {"id":2,"type":"update","typeLabel":"Обновление","date":"22.02.2026","title":"EternalBorder v2.0 — Стабильный релиз","text":"Полный рефакторинг плагина барьера.","tags":["EternalBorder","Барьер"]},
    {"id":3,"type":"announce","typeLabel":"Анонс","date":"23.02.2026","title":"Столица и система ПВП — в разработке","text":"Официально подтверждена новая концепция.","tags":["Столица","ПВП"]},
    {"id":4,"type":"event","typeLabel":"Событие","date":"19.02.2026","title":"Войны фракций — механика подтверждена","text":"Система городов и фракций.","tags":["Фракции"]}
]

def load_news():
    if NEWS_FILE.exists():
        try:
            content = NEWS_FILE.read_text(encoding="utf-8").strip()
            if content:
                data = json.loads(content)
                if isinstance(data, list):
                    return data
        except Exception as e:
            print(f"Warning: {e}")
    save_news(DEFAULT_NEWS)
    return DEFAULT_NEWS

def save_news(news):
    try:
        tmp = NEWS_FILE.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(news, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(NEWS_FILE)
    except Exception as e:
        print(f"Save error: {e}")

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

@app.get("/api/status")
def get_status():
    with _status_lock:
        data       = _status_cache["data"]
        updated_at = _status_cache["updated_at"]
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
        "id":        int(time.time() * 1000),
        "type":      data.get("type", "info"),
        "typeLabel": data.get("typeLabel", "Инфо"),
        "date":      data.get("date", ""),
        "title":     data.get("title", ""),
        "text":      data.get("text", ""),
        "tags":      data.get("tags", [])
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
    print(f"🔍 Пингуем {MC_HOST}:{MC_PORT} каждые 10 секунд (прямой socket)...")
    app.run(host="0.0.0.0", port=PORT)
