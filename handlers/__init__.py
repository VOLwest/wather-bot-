__all__ = ("router",)

from aiogram import Router

from .start import router as start_router
from .weather import router as weather_router

router = Router(name=__name__)

router.include_routers(
    start_router,
    weather_router,
)
