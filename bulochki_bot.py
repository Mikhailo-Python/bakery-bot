import telebot
from telebot import types

bot = telebot.TeleBot("8351581204:AAGtXnUjhyhtY7bH73EFsMBoxkOcrP51SZs")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Меню 🥐")
    btn2 = types.KeyboardButton("Де купити? 📍")
    btn3 = types.KeyboardButton("Ціни 💰")
    btn4 = types.Keyboardbutton("Замовити🛍️")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, "Ласкаво просимо до бота Іршанських булочок! Виберіть пункт меню:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "Меню 🥐":
        bot.send_message(message.chat.id, "У нас є:\n- З маком\n- З повидлом\n- З сиром\n- Знаменита булочка з корицею!")
    
    elif message.text == "Де купити? 📍":
        bot.send_message(message.chat.id, "Шукайте нас на автостанції та в центрі Іршанська!")
    
    elif message.text == "Ціни 💰":
        bot.send_message(message.chat.id, "Ціни починаються від 15 грн. Найсвіжіші — зранку!")
    
   elif message.text == "Замовити🛍️":
    msg =
bot.send_message(message.chat.id, "Напишіть, що саме ви хочете замовити і скільки?")
 
bot.register_next_step_handler(msg,send_order_to_me)

else:
    bot.send_message(message.chat.id, "Я просто бот, краще натисніть на кнопку!")

def send_order_to_me(message):
    my_id = 1312739397
    user_name =
    message.from_user.username if
    message.from_user.username else "Клієнт без ніка"

    bot.send_message(my_id, f"🔔 ЗАМОВЛЕННЯ від @{user_name}:\n{message.text}")
    bot.send_message(message.chat.id, "✅ Замовлення надіслано! Ми зв'яжемося з вами.")
    
bot.polling(none_stop=True)




