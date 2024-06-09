import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","27264326"))
    API_HASH = os.environ.get("API_HASH","eef640f8abe078ff5c89defa3195c5c1"))
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7494589224:AAHRyfLVLDziHzOcJs5a6vi9huKjUjwHLZs"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Tegerfl_bot"))
    BOT_NAME = os.environ.get("@Tegerfl_bot","Tegerfl_bot"))
    BOT_ID = int(os.environ.get("BOT_ID","7494589224"))
    SUDO_USERS = os.environ.get("SUDO_USERS").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","-1002028970832"))
    OWNER_ID = int(os.environ.get("OWENER_İD","6070918315"))
    OWNER_USERNAME = os.environ.get("felask","felask"))
