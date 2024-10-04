from pyrogram import Client, filters
from flask import Flask
import threading
import os

# Flask app
app = Flask(__name__)

# Pyrogram Bot configuration
api_id = os.environ.get("27317700")
api_hash = os.environ.get("de1077f45e29e6abebcd2b9dd196be1d")
bot_token = os.environ.get("BOT_TOKEN")

# Pyrogram Client
bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Telegram Bot Command Handler for /start
@bot.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Hello! This bot is active and running!")  # Simplified response

# Flask route for health check
@app.route("/")
def index():
    return "Bot is running on Flask!"

def run_bot():
    bot.run()

if __name__ == "__main__":
    # Running Flask app in main thread
    app.run(host="0.0.0.0", port=8080)

    # Running Telegram bot in a separate thread
    t2 = threading.Thread(target=run_bot)
    t2.start()
