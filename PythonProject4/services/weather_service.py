
import requests
from config import API_KEY

async def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return "Город не найден. Попробуйте еще раз."

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    return (f"Погода в {city}:\n"
            f"Описание: {weather}\n"
            f"Температура: {temp}°C\n"
            f"Влажность: {humidity}%\n"
            f"Скорость ветра: {wind} м/с")