import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "17877878"))
  API_HASH = os.environ.get("API_HASH", "adade73fc0c2f43855ef2a44a22576b4")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6797342276:AAFgAw_4XGmYN2fk_klmx2vAjZGoP6pXEcw")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "PrincessMassacrebot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002032273289"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "moneykamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "80362d2ec111bac371800e90e97df859d8ef0763")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1271227004"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://zerocodde:zerocodde@cluster0.rfgq5du.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002126809729")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002032273289"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [ZeroCodde](https://telegram.me/zerocodde)
)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

*CURRENTLY WORKING FOR @DINOMOVIESTG*

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.
"""
