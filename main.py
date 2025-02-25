# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import bot_token
from handlers import router as main_router

# Добавлен парс-мод на HTML (для работы с текстом)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode="HTML"))

# Создание основной функции для обновления и диспатчеров
async def main():
    # Подключение главного маршрутизатора
    dp.include_router(main_router)

    # Включение опроса бота
    await dp.start_polling(bot)

# Включение асинхронного потока
if __name__ == '__main__':
    asyncio.run(main())
