from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "25587869"))
API_HASH = getenv("API_HASH", "be4ae8dc41f4d81f970cbf88b9f3a36b")

BOT_TOKEN = getenv("BOT_TOKEN", "6187521001:AAHCtI-7kxBtUtps6JhDzar_fnV1mSy28l8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "1892884368"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/90904693bbfdf2380e680.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/90904693bbfdf2380e680.jpg")

SESSION = getenv("SESSION", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+YPmO3VrxpYJhMGZl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MyraNetwork")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1892884368").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
