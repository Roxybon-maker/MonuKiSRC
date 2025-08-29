# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "24663422"))
API_HASH = getenv("API_HASH", "723918463d17ff94e655e2cc53513c61")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8431889657").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://technicalboy871_db_user:GBANnC6od28XtMn1@cluster0.rmkdrks.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002955826058")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002955826058"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000"))
WEBSITE_URL = getenv("WEBSITE_URL", "arolinks.com")
AD_API = getenv("AD_API", "774f4f3173cfcc6b1c17d574164abeb1addc27c9")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
