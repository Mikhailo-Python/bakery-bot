import telebot
from telebot import types
import os
import json

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

with open('menu.json', 'r', encoding='utf-8') as f:
    menu_data = json.load(f)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Меню 🥐")
    btn2 = types.KeyboardButton("Де купити? 📍")
    btn3 = types.KeyboardButton("Ціни 💰")
    btn4 = types.KeyboardButton("Замовити 📦")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Ласкаво просимо до бота Іршанських булочок! Виберіть пункт меню:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "Меню 🥐":
        names = ", ".join([item['name'] for item in menu_data.values()])
        bot.send_message(message.chat.id, f"У нас є: {names}")

    elif message.text == "Де купити? 📍":
        bot.send_message(message.chat.id, "Шукайте нас на автостанції та в центрі Іршанська!")

    elif message.text == "Ціни 💰":
        # Тут тепер одинарні лапки для ключів — це важливо!
        prices_list = "\n".join([f"{v['name']} — {v['price']} грн" for v in menu_data.values()])
        bot.send_message(message.chat.id, f"Наші ціни сьогодні:\n{prices_list}")

    elif message.text == "Замовити 📦":
        msg = bot.send_message(message.chat.id, "Напишіть, що саме ви хочете замовити і скільки?")
        bot.register_next_step_handler(msg, send_order_to_me)

    else:
        bot.send_message(message.chat.id, "Я просто бот, краще натисніть на кнопку! 😊")

def send_order_to_me(message):
    my_id = 1312730397
    user_info = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
    
    bot.send_message(my_id, f"🔔 НОВЕ ЗАМОВЛЕННЯ!\nВід: {user_info}\nТекст: {message.text}")
    # Підтверджуємо клієнту
    bot.send_message(message.chat.id, "✅ Замовлення прийнято! Скоро зв'яжемося.")

bot.polling(none_stop=True)























