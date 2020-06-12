import telebot
import mysql
import Mytoken

from datetime import time
from datetime import datetime
from telebot import apihelper
sekarang = datetime.now()
TOKEN = Mytoken.TOKEN
mybot = telebot.TeleBot(TOKEN)

class MyBot:
    def __init__(self):
        self.message

    @mybot.message_handler(commands=['start', 'help'])
    def start(message):
        #photo = open('img/rpl.png, rb')
        teks = Mytoken.SAPA + "\n-- Admin & dev Adhi satria banyuaji --" + "\n" \
                                "-- Hari ini tanggal " + str(sekarang) + " --"
        mybot.reply_to(message, teks)

    @mybot.message_handler()

print("Bot sudah berjalan bro...")
mybot.polling(none_stop=True)

