import telebot
from telebot import types

TOKEN = '7673908089:AAEycNk2sLzXaaDllb54qbQtgJFJReN8G_Q'
bot = telebot.TeleBot(TOKEN)

main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
catalog_button = types.KeyboardButton('Catalog🗃️')
basket_button = types.KeyboardButton('Coș 🛒')
orders_button = types.KeyboardButton('Comenzi🚚')
feedback_button = types.KeyboardButton('FeedBack💭')
main_markup.add(catalog_button, basket_button, orders_button, feedback_button)

@bot.message_handler(commands=['start'])
def start(message):
    send_message = "<b>Salut 👋</b>\nBine ați venit la magazinul nostru online!"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=main_markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Log the user message to the console
    print(f"User {message.from_user.username} ({message.from_user.id}) sent: {message.text}")

    if message.text == 'Catalog🗃️':
        catalog_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        motherboard_button = types.KeyboardButton('Plăci de bază 🔗')
        gpu_button = types.KeyboardButton('Plăci video 🎮')
        cpu_button = types.KeyboardButton('Procesoare 🧠')
        ram_button = types.KeyboardButton('Memorii RAM 🎟')
        psu_button = types.KeyboardButton('Surse de alimentare ⚡')
        storage_button = types.KeyboardButton('HDD,SDD 💿')
        cooling_button = types.KeyboardButton('Sisteme de răcire 🧊')
        case_button = types.KeyboardButton('Carcase 🖥')
        back_button = types.KeyboardButton('Înapoi▶️')
        catalog_markup.add(motherboard_button, gpu_button, cpu_button, ram_button, psu_button, storage_button, cooling_button, case_button, back_button)
        send_message = "Minunat! Ce anume vă înteresează?"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=catalog_markup)

    elif message.text == "Plăci de bază 🔗":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/placi-de-baza")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Plăci video 🎮":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/placi-video")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Procesoare 🧠":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/procesoare")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Memorii RAM 🎟":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/memorii-ram")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Surse de alimentare ⚡":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/surse")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "HDD,SDD 💿":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/stocare")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Sisteme de răcire 🧊":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/racire")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == "Carcase 🖥":
        markup = types.InlineKeyboardMarkup()
        unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/carcase")
        markup.add(unity)
        send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
        bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    elif message.text == 'Înapoi▶️':
        bot.send_message(message.chat.id, "Înapoi la meniul principal.", reply_markup=main_markup)

    elif message.text == 'Coș 🛒':
        send_message = "Coșul dvs. este momentan gol. Adăugați produse din catalog!"
        bot.send_message(message.chat.id, send_message, parse_mode='html')

    elif message.text == 'Înapoi▶️':
        bot.send_message(message.chat.id, "Înapoi la meniul principal.", reply_markup=main_markup)

    elif message.text == "Comenzi🚚":
        send_message = "Aici puteți vedea și gestiona comenzile dumneavoastră, Mulțumim că nea-ți ales!"
        bot.send_message(message.chat.id, send_message, parse_mode='html')

    elif message.text == 'Înapoi▶️':
        bot.send_message(message.chat.id, "Înapoi la meniul principal.", reply_markup=main_markup)

    elif message.text == "FeedBack💭":
        bot.send_message(message.chat.id, "Vă rugăm să ne spuneți părerea dvs. despre serviciile noastre. Vom fi bucuroși să aflăm ce putem îmbunătăți!")
        bot.register_next_step_handler(message, receive_feedback)

def receive_feedback(message):
    feedback = message.text
    bot.send_message(message.chat.id, "Mulțumim pentru feedback-ul tău! Îți mulțumim că ne ajuți să îmbunătățim serviciile noastre.")
    bot.send_message(message.chat.id, "Înapoi la meniul principal.", reply_markup=main_markup)


try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Bot polling failed: {e}")
