from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
import threading
import os
import logging
import asyncio

# Setup logging
logging.basicConfig(level=logging.INFO)

# Flask app
app = Flask(__name__)

# Pyrogram Bot configuration
api_id = os.environ.get("API_ID")  # Get API ID from environment variable
api_hash = os.environ.get("API_HASH")  # Get API hash from environment variable
bot_token = os.environ.get("BOT_TOKEN")  # Get bot token from environment variable

# Pyrogram Client
bot = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
)

# Telegram Bot Command Handler for /start
@bot.on_message(filters.command("start"))
def start_command(client, message):
    logging.info("Received /start command")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Free Shop", callback_data="free_shop")],
        [InlineKeyboardButton("Paid Shop", callback_data="paid_shop")]
    ])
    message.reply_text("Welcome to the Shop Bot! Choose an option:", reply_markup=keyboard)

# Callback query handler
@bot.on_callback_query()
def handle_callback_query(client, callback_query):
    if callback_query.data == "free_shop":
        callback_query.message.reply_text("Welcome to the Free Shop!")
    elif callback_query.data == "paid_shop":
        callback_query.message.reply_text("Welcome to the Paid Shop!")

# Flask route for health check
@app.route("/")
def index():
    return "Bot is running on Flask!"

def run_bot():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bot.run()
    except Exception as e:
        logging.error(f"Pyrogram Error: {e}")

if __name__ == "__main__":
    # Running Telegram bot in a separate thread
    t2 = threading.Thread(target=run_bot)
    t2.start()
    
    # Running Flask app in main thread
    app.run(host="0.0.0.0", port=8080)
