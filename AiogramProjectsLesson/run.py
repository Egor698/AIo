from aiogram import Dispatcher, Bot
import asyncio
from app import handlers


async def start():

    bot = Bot('8099627872:AAH-DKApph91euYAPrHrUWobsACoJxQT9tk')
    
    dp = Dispatcher()

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    
    handlers.include_routers(dp)

    await dp.start_polling(bot)


async def startup():
    print('Start')


async def shutdown():
    print('Stop')


if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        pass