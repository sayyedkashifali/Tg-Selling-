import telebot
from telebot import types

# Your Telegram Bot Token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = telebot.TeleBot(TOKEN)

# Placeholder for product information (we'll improve this later)
products = {
    'product1': {
        'name': 'Product 1',
        'description': 'This is a fantastic product!',
        'image_url': 'https://example.com/product1.jpg'  # Replace with your image URL
    },
    'product2': {
        'name': 'Product 2',
        'description': 'Another amazing product!',
        'image_url': 'https://example.com/product2.jpg'
    }
}

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('/products')
    itembtn2 = types.KeyboardButton('/support')
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, "Welcome! I'm your selling bot. Choose an option:", reply_markup=markup)

# Handle the /products command
@bot.message_handler(commands=['products'])
def show_products(message):
    markup = types.InlineKeyboardMarkup()
    for product_id, product in products.items():
        button = types.InlineKeyboardButton(product['name'], callback_data=product_id)
        markup.add(button)
    bot.reply_to(message, "Here are our products:", reply_markup=markup)

# Handle button clicks for products
@bot.callback_query_handler(func=lambda call: True)
def handle_product_click(call):
    product_id = call.data
    product = products.get(product_id)
    if product:
        # Send product details
        caption = f"{product['name']}\n\n{product['description']}"
        bot.send_photo(call.message.chat.id, product['image_url'], caption=caption)
        # Here you can add the payment process later
        bot.send_message(call.message.chat.id, "Payment system coming soon!")
    else:
        bot.answer_callback_query(call.id, "Invalid product selected.")

# Handle the /support command
@bot.message_handler(commands=['support'])
def provide_support(message):
    bot.reply_to(message, "Contact support at [your support email or channel]")

# Start listening for messages
bot.polling()
