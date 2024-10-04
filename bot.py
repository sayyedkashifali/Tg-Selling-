import telebot
import os

# Access the bot token from environment variables
BOT_TOKEN = os.environ.get('7734029404:AAGjciB3zvBfxMP8XpePT3-mRQLsPAkCY74') 

bot = telebot.TeleBot(BOT_TOKEN)

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! Products will be added soon.")

# Start listening for messages
bot.polling()
