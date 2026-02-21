import telebot
from telebot import types

bot = telebot.TeleBot("8351581204:AAGtXnUjhyhtY7bH73EFsMBoxkOcrP51SZs")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Меню 🥐")
    btn2 = types.KeyboardButton("Де купити? 📍")
    btn3 = types.KeyboardButton("Ціни 💰")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, "Ласкаво просимо до бота Іршанських булочок! Виберіть пункт меню:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "Меню 🥐":
        bot.send_message(message.chat.id, "У нас є:\n- З маком\n- З повидлом\n- З сиром\n- Знаменита булочка з корицею!")
    
    elif message.text == "Де купити? 📍":
        bot.send_message(message.chat.id, "Шукайте нас на автостанції та в центрі Іршанська!")
    
    elif message.text == "Ціни 💰":
        bot.send_message(message.chat.id, "Ціни починаються від 15 грн. Найсвіжіші — зранку!")
    
    else:
        bot.send_message(message.chat.id, "Я просто бот, краще натисніть на кнопку!")

bot.polling()