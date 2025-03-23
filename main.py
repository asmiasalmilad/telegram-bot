from flask import Flask, request
from rembg import remove

from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import os

app = Flask(__name__)

# دریافت توکن‌ها از متغیرهای محیطی
TELEGRAM_BOT_TOKEN = os.getenv("8058193815:AAG3jrAbJwjiuxC24QC-PSPJO4uIqf-fzJI")
REMOVE_BG_API_KEY = os.getenv("xSEQMVAWQTPzL3GfkJzzshjA")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
rmbg = RemoveBg(REMOVE_BG_API_KEY)

@app.route("/")
def home():
    return "Telegram Bot is running!"

def start(update, context):
    update.message.reply_text("سلام! من می‌تونم بک‌گراند عکس رو حذف کنم. عکس رو بفرست!")

def remove_background(update, context):
    file = update.message.photo[-1].get_file()
    file_path = "input.jpg"
    output_path = "output.png"

    file.download(file_path)
    rmbg.remove_background_from_img_file(file_path, output_path)

    context.bot.send_photo(chat_id=update.message.chat_id, photo=open(output_path, "rb"))

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, remove_background))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
