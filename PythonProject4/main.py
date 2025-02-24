# main.py
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()

register_handlers(dp)

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True, bot=bot)