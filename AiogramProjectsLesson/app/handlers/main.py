from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from aiogram.filters import CommandStart
import app.keyboards.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_main(msg: Message):
    
    await msg.answer(text='Добро пожаловать в магазин кросовок!',
                     reply_markup=kb.main)