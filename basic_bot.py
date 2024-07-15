from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, Application, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! This is your bot.')


def main():
    application = Application.builder().token('7207211741:AAGStHm1qskhdyDypOa_dJc_Sd00BDLBq74').build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.run_polling()

if __name__ == '__main__':
        main()


