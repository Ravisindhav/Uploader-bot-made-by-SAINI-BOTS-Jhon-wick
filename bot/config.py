import os
import urllib.parse
from dotenv import load_dotenv
load_dotenv("config.env")
username = "db_sindhavravi11@gmail.com"
password = "db_$Ravi1996"
cluster_name = "cluster0.bwlgbx3.mongodb.net"
quoted_username = urllib.parse.quote_plus(username)
quoted_password = urllib.parse.quote_plus(password)
DATABASE_URL = f"mongodb+srv://{quoted_username}:{quoted_password}@{cluster_name}/?retryWrites=true&w=majority&appName=Cluster0"
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "tg_bot")
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
WEB_SERVER = os.environ.get("WEB_SERVER", "False") == "True"
WEBHOOK = True
PORT = int(os.environ.get("PORT", 8000))
THUMBNAILS = os.environ.get("THUMBNAILS", "https://i.imgur.com/6c9F05x.png")
class Config(object):
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    DATABASE_NAME = DATABASE_NAME
    DATABASE_URL = DATABASE_URL
    OWNER_ID = OWNER_ID
    LOG_CHANNEL = LOG_CHANNEL
    WEB_SERVER = WEB_SERVER
    WEBHOOK = WEBHOOK
    PORT = PORT
    THUMBNAILS = THUMBNAILS

    # Constants
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):
    START_MESSAGE = (
        " {mention}\n\nsᴇɴᴅ ᴀɴʏ ʟɪɴᴋ ᴏʀ ᴛxᴛ ғɪʟᴇ."
    )
    DEV_MESSAGE = """👋 Hey there, I'm [sᴀɪɴɪ ʙᴏᴛs](https://t.me/saini_contact_bot)) – your go-to Telegram bot developer!

🤖 Love having bots that do the heavy lifting for you? That's my jam! I'm all about crafting super cool and custom Telegram bots that make your life a breeze.

✨ **What I Do**

- **Bot Magic:** From automating tasks to interactive games, I create bots that do it all. Seriously, ask me anything!
- **Tailored to You:** Your bot, your rules. I'll whip up a bot that's as unique as you are.
- **Chill Vibes:** I keep your data super safe, so you can relax and enjoy the bot party.
- **Always Improving:** Telegram evolves, and my bots grow with it. I'm here to keep things fresh and fab.

Ready for your own bot buddy? Ping me on [Telegram](https://t.me/1234) or check out me on [GitHub](https://github.com/1234). Wanna hire me?

Let's bot up and have some fun! 🤘"""
    HELP_MESSAGE = os.environ.get("HELP_MESSAGE", "Help message")
    PROGRESS_MESSAGE = """**╔════❰ Uploading ❱══❍
║╭━➣
║┣⪼  Progress:-  {percentage}%
║┣ 
║┣⪼ {progress}
║┣
║┣⪼《{finished} of {total}》
║┣ 
║┣⪼ Speed:- {speed}/s
║┣ 
║┣⪼ ETA:- {eta} 
║╰━➣
╚════════════════❍**"""
    NEW_USER_MESSAGE = """#NewUser

🆔 User ID: `{user_id}`
👤 User: {mention}
"""
    DOWNLOADING = """📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥 
    
📟 {start_index}/{end_index}

📝 Name » {link_no} » {name}

🔢Index: {orginal_start_index}/{orginal_end_index}

...sᴀɪɴɪ ʙᴏᴛs..."""

    DEFAULT_CAPTION = """[📁] File_ID : {file_index}

𖤓 𝐓ɪᴛʟᴇ  : {file_name}

🗃 𝐒𝐢𝐳𝐞 : {file_size}

📚 Bᴀᴛᴄʜ Nᴀᴍᴇ : {batch_name}

🌟 Exᴛʀᴀᴄᴛᴇᴅ Bʏ : [𝄟⃝‌sᴀɪɴɪ ʙᴏᴛs𝄟⃝‌](https://t.me/saini_contact_bot)"""


    CAPTION_CB = """**Set Caption

➢ Available Variables 👇**

┌🎴 𝐍𝐚𝐦𝐞 : `{file_name}`
├🗃 𝐒𝐢𝐳𝐞 : `{file_size}`
├⚙️ 𝐄𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧 : `{file_extension}`
├🧭 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 : `{file_duration}`
├🖇 𝐋𝐢𝐧𝐤 : `{file_url}`
├🔢 𝐈𝐧𝐝𝐞𝐱 : `{file_index}`
├🗳 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞 : `{batch_name}`

==============================

➢ Current:
`{current_caption}`

==============================

➢ **Default:**
`{default_caption}`

➢ **Status:** {status}"""
