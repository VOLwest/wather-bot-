# handlers/__init__.py
from .start import register_start_handlers
from .weather import register_weather_handlers

def register_handlers(dp):
    register_start_handlers(dp)
    register_weather_handlers(dp)