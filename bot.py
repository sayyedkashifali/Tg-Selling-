import os
import time
import telebot

# Access the bot token from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! Products will be added soon.")

# Start listening for messages with error handling and retry mechanism
while True:
    try:
        # Removed host and port arguments for Koyeb deployment
        bot.polling(none_stop=True, timeout=60)  
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(15)  # Wait before retrying
