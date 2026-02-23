from aiogram import Dispatcher
from app.handlers.main import router as router_main
from app.handlers.catalog import router as router_info
from app.handlers.cart import router as router_cart

def include_routers(dp: Dispatcher):
    dp.include_routers(router_main, router_info, router_cart)
