import os
from pymongo import MongoClient
from telegram.ext import Updater, CommandHandler

# 🟢 Get Mongo URI & Token from environment
MONGO_URI = os.getenv("MONGO_URI")
TOKEN = os.getenv("TOKEN")

# ✅ Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["telegram_bot"]  # Or whatever your DB name is
collection = db["messages"]

# 🟡 Start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="✅ Bot chal gaya hai!")

# 🔁 Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
