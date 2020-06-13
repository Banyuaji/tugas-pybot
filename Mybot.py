import telebot
import mysql.connector
import Mytoken

from datetime import datetime
from telebot import apihelper
sekarang = datetime.now()
TOKEN = Mytoken.TOKEN
mybot = telebot.TeleBot(TOKEN)
myDB = mysql.connector.connect(host='localhost', user='root', database='db_belajarbot')
sql = myDB.cursor()

class MyBot:
    def __init__(self):
        self.message

    @mybot.message_handler(commands=['start', 'help'])
    def start(message):
        photo = open('img/rpl.png', 'rb')
        mybot.send_photo(message.from_user.id, photo)
        teks = Mytoken.SAPA + "\n-- Admin & dev Adhi satria banyuaji --" + "\n" \
                                "-- Hari ini tanggal " + str(sekarang) + " --"
        mybot.reply_to(message, teks)

    @mybot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if (jmldata > 0):
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x) + "\n"
                kumpuldata = kumpuldata.replace('(', str(no) + '. ')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
                print(kumpuldata)
        else:
            print('data kosong')

        mybot.reply_to(message, str(kumpuldata))

print("Bot sudah jalan bro...")
mybot.polling(none_stop=True)

