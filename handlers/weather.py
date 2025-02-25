import aiohttp
from aiogram import Router, types
from aiogram.filters import Command

from config import api_key

# Создание роутера для подключения его
router = Router(name=__name__)


@router.message(Command('weather', prefix='/', ignore_case=True))
async def cmd_weather(message: types.Message):
    args = message.text.split(maxsplit=1)
    city = args[1] if len(args) > 1 else None

    if not city:
        await message.answer("Пожалуйста, укажите город. Например: /weather Москва")
        return

    weather_data = await get_weather(city)
    await message.answer(weather_data)


async def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    if data["cod"] != 200:
        return "Город не найден. Попробуйте еще раз."

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    return (f"Погода <b>{city.lower().capitalize()}</b>\n"
            f"☁️Погода: <b>{weather}</b>\n"
            f"🌡Температура: <b>{temp}°C</b>\n"
            f"💧Влажность: <b>{humidity}%</b>\n"
            f"💨Скорость ветра: <b>{wind} м/с</b>")