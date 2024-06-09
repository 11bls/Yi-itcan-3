
import telebot
from pytube import YouTube
from youtubesearchpython import VideosSearch
import os
import time
from datetime import datetime

TOKEN = '6552075227:AAECRZ4bBHmzpWlyKuVCKxDhFbpQvneK7Yc'

bot = telebot.TeleBot(TOKEN)

print(f"\x1b[1;34m#FREE ALTYAPI BOŞ BİRSEY ZATEN KUMAR BOTU GİBİ SATIŞ YAPMAYA CALIŞAN ELEMANLARIN ANASINI SİKEYİM BOT AKTİF")

@bot.message_handler(commands=['start'])
def start(message):
    fahise_karilar = datetime.now().hour
    if 5 <= fahise_karilar < 12:
        ramazan = "Günaydın 🥱"
    elif 12 <= fahise_karilar < 17:
        ramazan = "İyi öğlenler 🫠"
    elif 17 <= fahise_karilar < 22:
        ramazan = "İyi akşamlar 🤤"
    else:
        ramazan = "İyi geceler 😴"

    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    button1 = telebot.types.InlineKeyboardButton("Sahibim ❤️‍🩹", url="https://t.me/zirvebenimyerim")
    button2 = telebot.types.InlineKeyboardButton("Komutlar 💋", callback_data="ramazan")
    button3 = telebot.types.InlineKeyboardButton("Kanal 😍", url="https://t.me/tryepayzeka")
    markup.add(button1, button2, button3)
    bot.reply_to(message, f"{ramazan} Ben müzik indirme botuyum, beni tercih ettiğiniz için teşekkür ederim.", reply_markup=markup)

@bot.message_handler(commands=['indir'])
def download_music(message):
    query = " ".join(message.text.split()[1:])
    search_and_send_music(message, query)

def search_and_send_music(message, query):
    videosSearch = VideosSearch(query, limit=1)
    result = videosSearch.result()

    if result["result"]:
        video_url = result["result"][0]["link"]

        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(only_audio=True).first()

            path = stream.download(output_path=".", filename=yt.title)

            search_message = bot.send_message(message.chat.id, f"🔎 İstediğiniz parça aranıyor...")
            
            time.sleep(2)
            bot.delete_message(message.chat.id, search_message.message_id)
            
            search_message = bot.send_message(message.chat.id, f"⏳ İstediğiniz parça indiriliyor.")
            
            time.sleep(2)
            bot.delete_message(message.chat.id, search_message.message_id)

            with open(path, 'rb') as media:
                caption = f"✦ Parça: {yt.title}                                                                           ✦ İsteyen: @{message.from_user.username}"
                bot.send_audio(message.chat.id, media, caption=caption)

            os.remove(path)
        except Exception as e:
            bot.reply_to(message, "İstediğiniz parça bulunamadı 🥲")
    else:
        bot.reply_to(message, "İstediğiniz parça bulunamadı 🥲")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "ramazan":
        bot.send_message(call.message.chat.id, "🍓 Komutlar;\n/start - Botu Başlatır 💓\n/indir - Müzik indirir 🥰")

bot.polling(none_stop=True)
