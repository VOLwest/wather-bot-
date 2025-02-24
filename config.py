# config.py
from os import getenv
from dotenv import load_dotenv

# Загружаем переменные из локального окружения
load_dotenv(".env")

# Токены от ботов телеграмма
bot_token = getenv("BOT_TOKEN")
api_key = getenv("API_KEY")
