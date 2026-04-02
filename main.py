# ============================================================
# Group Manager Bot
# ============================================================

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
import threading
import os
from flask import Flask

# 🔐 Security
from security import verify_integrity, get_runtime_key

logging.basicConfig(level=logging.INFO)

verify_integrity()
RUNTIME_KEY = get_runtime_key()

# ================== 🌐 Flask Web Server ==================

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Natasha Group Bot Running 🚀"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    web_app.run(host="0.0.0.0", port=port)

# Start web server in background
threading.Thread(target=run_web).start()

# ================== 🤖 Telegram Bot ==================

app = Client(
    "group_manager_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from handlers import register_all_handlers
register_all_handlers(app)

print("✅ Bot is starting securely...")

app.run()
