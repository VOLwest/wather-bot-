# handlers.py
from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    # Регистрация обработчика команды /start
    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        await message.reply("Привет! Я бот.")

    # Регистрация обработчика для текстовых сообщений
    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer(message.text)