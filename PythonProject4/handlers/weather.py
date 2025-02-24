
from aiogram import types
from aiogram.dispatcher import Dispatcher
from services.weather_service import get_weather

async def cmd_weather(message: types.Message):
    city = message.get_args()
    if not city:
        await message.answer("Пожалуйста, укажите город. Например: /weather Москва")
        return

    weather_data = await get_weather(city)
    await message.answer(weather_data)

def register_weather_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_weather, commands="weather")