import telebot
from pyexpat.errors import messages
from telebot import types

TOKEN = '7673908089:AAEycNk2sLzXaaDllb54qbQtgJFJReN8G_Q'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    catalog = types.KeyboardButton('Catalog🗃️')
    basket = types.KeyboardButton('Coș🗑️')
    orders = types.KeyboardButton('Comenzi🚚')
    feedback = types.KeyboardButton('FeedBack💭')

    markup.add(catalog, basket, orders, feedback)

    send_message = "<b>Salut 👋</b>\nBine ați venit la magazinul nostru online!"
    bot.send_message(message.chat.id, send_message,parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == "Catalog🗃️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        motherboard = types.KeyboardButton('Plăci de bază 🔗')
        gpu = types.KeyboardButton('Plăci video 🎮')
        cpu = types.KeyboardButton('Procesoare 🧠')
        ram = types.KeyboardButton('Memorii RAM 🎟')
        psu = types.KeyboardButton('Surse de alimentare ⚡')
        storage = types.KeyboardButton('HDD,SDD 💿')
        cooling = types.KeyboardButton('Sisteme de răcire 🧊')
        case = types.KeyboardButton('Carcase 🖥')
        back = types.KeyboardButton('Înapoi▶️')
        markup.add(motherboard, gpu, cpu, ram, psu, storage, cooling, case, back)
        send_message = "Minunat! Ce anume vă înteresează?"
        bot.send_message(message.chat.id, send_message,parse_mode='html', reply_markup=markup)
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
     unity = types.InlineKeyboardButton("https://xstore.md/componente-pc/racire")
     markup.add(unity)
     send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Carcase 🖥'":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/carcase")
     markup.add(unity)
     send_message = "Cele mai noi componente sunt pe site-ul nostru Online"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Bot polling failed: {e}")