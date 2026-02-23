import hashlib
import hmac
import os
import time
from collections import defaultdict

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

# ── Config ────────────────────────────────────────────────────────
ADMIN_PASSWORD_HASH: str = os.getenv("ADMIN_PASSWORD_HASH", "").lower()
ALLOWED_ORIGIN: str      = os.getenv("ALLOWED_ORIGIN", "*")
PORT: int                = int(os.getenv("PORT", 3000))

# ── App ───────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app, origins=[ALLOWED_ORIGIN], methods=["POST", "OPTIONS"])

# ── Rate limit (in-memory) ────────────────────────────────────────
RATE_WINDOW = 60   # секунд
RATE_MAX    = 10   # попыток за окно

_rate_store: dict = defaultdict(lambda: {"count": 0, "reset_at": 0})

def check_rate_limit(ip: str) -> bool:
    now   = time.time()
    entry = _rate_store[ip]
    if now > entry["reset_at"]:
        entry["count"]    = 0
        entry["reset_at"] = now + RATE_WINDOW
    entry["count"] += 1
    return entry["count"] <= RATE_MAX

# ── Routes ────────────────────────────────────────────────────────
@app.post("/auth")
def auth():
    ip = request.headers.get("x-forwarded-for", request.remote_addr).split(",")[0].strip()

    if not check_rate_limit(ip):
        return jsonify({"ok": False, "error": "Too many requests"}), 429

    data     = request.get_json(silent=True) or {}
    password = data.get("password", "")

    if not password:
        return jsonify({"ok": False}), 400

    incoming_hash = hashlib.sha256(password.encode()).hexdigest()
    ok = hmac.compare_digest(incoming_hash, ADMIN_PASSWORD_HASH)

    return jsonify({"ok": ok}), 200 if ok else 401


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


# ── Run ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    if not ADMIN_PASSWORD_HASH:
        print("⚠️  ВНИМАНИЕ: ADMIN_PASSWORD_HASH не задан в .env!")
    else:
        print("✅ Auth server ready")
    app.run(host="0.0.0.0", port=PORT)
