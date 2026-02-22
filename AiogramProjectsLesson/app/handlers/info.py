from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from app.handlers.CallbackData import BrandCD, SneakersCD
import app.keyboards as kb
import app.handlers.pretty_info as pi

router = Router()

@router.callback_query(F.data=="back:Каталог")
@router.message(F.text=="Каталог")
async def cmd_info_brand(update: Message | CallbackQuery):
    if isinstance(update, CallbackQuery):
        
        await update.answer('')
        await update.message.delete()
        
        await update.message.answer(
            text='Выберите бренд',
            reply_markup=kb.gen_menu_info_brand()
        )
    else:
        await update.answer(
            text='Выберите бренд',
            reply_markup=kb.gen_menu_info_brand()
        )


@router.callback_query(BrandCD.filter())
async def cmd_info_sneakers(query: CallbackQuery, callback_data: BrandCD):
    
    await query.answer('')
    await query.message.delete()
    
    await query.message.answer(text='Выберите модель кроссовок',
                     reply_markup=kb.gen_menu_info_sneakers(callback_data.key_brand))
    
    
@router.callback_query(SneakersCD.filter())
async def cmd_info_sneaker(query: CallbackQuery, callback_data: SneakersCD):
    
    await query.answer('')
    await query.message.delete()
    
    key_brand, sneakers_id = callback_data.key_brand, callback_data.sneakers_id
    
    caption, photo_url = pi.get_info_and_photo_about_sneaker(key_brand, sneakers_id)
   
    await query.message.answer_photo(photo=photo_url,
            caption=caption,
            parse_mode="HTML",
            reply_markup=kb.gen_menu_info_sneaker(key_brand, sneakers_id))