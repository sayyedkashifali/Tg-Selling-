const TelegramBot = require('node-telegram-bot-api');
const token = process.env.BOT_TOKEN; // Get bot token from environment variable
const bot = new TelegramBot(token, { polling: true });

// Command Handler for /start
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  const opts = {
    reply_markup: {
      inline_keyboard: [
        [{ text: 'Free Shop', callback_data: 'free_shop' }],
        [{ text: 'Paid Shop', callback_data: 'paid_shop' }],
      ],
    },
  };
  bot.sendMessage(chatId, 'Welcome to the Shop Bot! Choose an option:', opts);
});

// Callback Query Handler
bot.on('callback_query', (callbackQuery) => {
  const msg = callbackQuery.message;
  if (callbackQuery.data === 'free_shop') {
    bot.sendMessage(msg.chat.id, 'Welcome to the Free Shop!');
  } else if (callbackQuery.data === 'paid_shop') {
    bot.sendMessage(msg.chat.id, 'Welcome to the Paid Shop!');
  }
});

// Start the bot
bot.on('polling_error', (error) => {
  console.error(error);
});
