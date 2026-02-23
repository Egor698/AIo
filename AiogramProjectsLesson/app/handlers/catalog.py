from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from app.handlers.CallbackData import BrandCD, SneakerCD
import app.keyboards.keyboards_catalog as kb_catalog
import app.handlers.pretty_info as pi

router = Router()

@router.callback_query(F.data=="back:Каталог")
@router.message(F.text=="Каталог")
async def cmd_info_brands(update: Message | CallbackQuery):
    if isinstance(update, CallbackQuery):
        
        await update.answer('')
        await update.message.delete()
        
        await update.message.answer(
            text='Выберите бренд',
            reply_markup=kb_catalog.menu_brands_in_catalog
        )
    else:
        await update.answer(
            text='Выберите бренд',
            reply_markup=kb_catalog.menu_brands_in_catalog
        )


@router.callback_query(BrandCD.filter())
async def cmd_info_sneakers(query: CallbackQuery, callback_data: BrandCD):
    
    await query.answer('')
    await query.message.delete()
    
    await query.message.answer(text='Выберите модель кроссовок',
                     reply_markup=kb_catalog.gen_menu_sneakers_in_catalog(callback_data.key_brand))
    
    
@router.callback_query(SneakerCD.filter())
async def cmd_info_sneaker(query: CallbackQuery, callback_data: SneakerCD):
    
    await query.answer('')
    await query.message.delete()
    
    key_brand, sneaker_id = callback_data.key_brand, callback_data.sneaker_id
    
    caption, photo_url = pi.get_info_about_sneaker_catalog(key_brand, sneaker_id)
   
    await query.message.answer_photo(photo=photo_url,
            caption=caption,
            parse_mode="HTML",
            reply_markup=kb_catalog.gen_menu_sneaker_in_catalog(key_brand, sneaker_id))