
from aiogram import Router, types
from aiogram.filters import Command

# Создание роутера для подключения его
router = Router(name=__name__)

# Обработчик команды /start
@router.message(Command('start', prefix='/', ignore_case=True))
async def cmd_start(message: types.Message):
    await message.answer(text="Привет! Я бот, который покажет тебе погоду в любом городе.")
