import telebot

TOKEN = "8058193815:AAG3jrAbJwjiuxC24QC-PSPJO4uIqf-fzJI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام عسل میلاد گفت بهت بگم خیلی دوستت داره")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
