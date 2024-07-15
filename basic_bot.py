import os

import requests
from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes
from dotenv import load_dotenv

load_dotenv('token.env')
load_dotenv('server_address.env')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = requests.get(f'{os.getenv("server_addr")}/start')
    await update.message.reply_text(message.json()["Message"])

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = requests.get(f'{os.getenv("server_addr")}/test')
    await update.message.reply_text(message.json()["Message"])



def main():
    application = Application.builder().token(os.getenv("token")).build()
    start_handler = CommandHandler('start', start)
    info_handler = CommandHandler('test', test)
    application.add_handler(info_handler)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
