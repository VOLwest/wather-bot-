
from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards.main_menu import get_main_menu

async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, который покажет тебе погоду в любом городе.", reply_markup=get_main_menu())

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")