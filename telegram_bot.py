from pymongo import MongoClient
from telegram.ext import Updater, CommandHandler, MessageHandler
client = MongoClient("mongodb+srv://sindhavravi11:%24Sind1234567890@cluster0.bwlgbx3.mongodb.net/")
TOKEN = 'aapka_telegram_bot_token'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Bot chal gaya hai!')
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
