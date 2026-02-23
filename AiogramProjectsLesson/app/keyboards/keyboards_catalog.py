from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder


from data.catalog_data import CATALOG

from app.handlers.CallbackData import BrandCD, SneakerCD, RequestSneakerInCartCD


#клавиатуры модуля info
def gen_menu_brands_in_catalog():
    kb = InlineKeyboardBuilder()
    
    for key_brand, text in CATALOG.iter_key_brand_and_text_kb():
        kb.add(InlineKeyboardButton(text=text, callback_data=BrandCD(key_brand=key_brand).pack()))
        
    return kb.adjust(2).as_markup()

menu_brands_in_catalog = gen_menu_brands_in_catalog()


def gen_menu_sneakers_in_catalog(key_brand: str):
    kb = InlineKeyboardBuilder()
    
    for sneaker_id, text in CATALOG.iter_sneaker_id_and_text_kb(key_brand):
        kb.add(InlineKeyboardButton(text=text,
                callback_data=SneakerCD(key_brand=key_brand, sneaker_id=sneaker_id).pack()))  
        
    kb = kb.adjust(2)
    
    kb.row(
        InlineKeyboardButton(text='< Назад', callback_data='back:Каталог')
    )
        
    return kb.as_markup()
    
    
def gen_menu_sneaker_in_catalog(key_brand: str, sneaker_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='В корзину', style='success', callback_data=RequestSneakerInCartCD(sneaker_id=sneaker_id, key_brand=key_brand).pack())],
        [InlineKeyboardButton(text='< Назад', callback_data=BrandCD(key_brand=key_brand).pack())]
    ])
    
    
