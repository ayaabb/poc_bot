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

async def store_random_num(update:Update,context:ContextTypes.DEFAULT_TYPE):
    response = requests.get(f'{os.getenv("server_addr")}/generate')
    if response.status_code == 200:
        data = response.json()
        await update.message.reply_text(f"Number generated and saved: {data['number']}")
    else:
        await update.message.reply_text(response.content.decode())


def main():
    application = Application.builder().token(os.getenv("token")).build()
    start_handler = CommandHandler('start', start)
    test_handler = CommandHandler('test', test)
    generate_handler = CommandHandler('generate', store_random_num)
    application.add_handler(test_handler)
    application.add_handler(start_handler)
    application.add_handler(generate_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
