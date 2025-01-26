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
        gpu = types.KeyboardButton('Plăci video')
        cpu = types.KeyboardButton('Procesoare 🧠')
        ram = types.KeyboardButton('Memorii RAM 🎟')
        psu = types.KeyboardButton('Surse de alimentare ⚡')
        storage = types.KeyboardButton('HDD,SDD 💿')
        cooling = types.KeyboardButton('Sisteme de răcire 🧊')
        case = types.KeyboardButton('Carcase 🖥')
        markup.add(motherboard, gpu, cpu, ram, psu, storage, cooling, case)
        send_message = "Minunat! Ce anume vă înteresează?"
        bot.send_message(message.chat.id, send_message,parse_mode='html', reply_markup=markup)
    elif message.text == "Plăci de bază":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://xstore.md/componente-pc/placi-de-baza")
     markup.add(unity)
     send_message = "Cele mai noi componente "
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Blugi 👖":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://bizu.md/product-category/imbracaminte-pentru-barbati/blugi-pentru-barbati/")
     markup.add(unity)
     send_message = "Înntrraga colecție poate fi vizualizată pe site-ul nostru👀"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Încălțăminte 👟":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://intertop.kz/brands/")
     markup.add(unity)
     send_message = "Înntrraga colecție poate fi vizualizată pe site-ul nostru👀"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Cămeși 👔":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://tagaer.md/barbati/imbracaminte/camase/")
     markup.add(unity)
     send_message = "Înntrraga colecție poate fi vizualizată pe site-ul nostru👀"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Costume 🤵":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://ionel.md/ro/magazin/imbracaminte-clasica-pentru-barbati/")
     markup.add(unity)
     send_message = "Înntrraga colecție poate fi vizualizată pe site-ul nostru👀"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    elif message.text == "Rochii 👗":
     markup = types.InlineKeyboardMarkup()
     unity = types.InlineKeyboardButton("Accesați", url="https://cosanzeana.md/shop/")
     markup.add(unity)
     send_message = "Înntrraga colecție poate fi vizualizată pe site-ul nostru👀"
     bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Bot polling failed: {e}")