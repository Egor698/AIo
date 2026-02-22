from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.cart import CART
from data.catalog import CATALOG
from data.catalog import DataSneakers


from app.handlers.CallbackData import BrandCD, SneakersCD, RequestSneakerInCartCD, SneakersInCartCD



main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина')]
    
], input_field_placeholder='Выберите нужную вкладку', resize_keyboard=True)


def gen_menu_info_brand():
    kb = InlineKeyboardBuilder()
    
    for brand_key, info in CATALOG.items():
        kb.add(InlineKeyboardButton(text=info['text'], callback_data=BrandCD(key_brand=brand_key).pack()))
        
    return kb.adjust(2).as_markup()


def gen_menu_info_sneakers(key_brand: str):
    kb = InlineKeyboardBuilder()
    
    for info in CATALOG[key_brand]['items']:
        kb.add(InlineKeyboardButton(text=info['text'],
                callback_data=SneakersCD(key_brand=key_brand, sneakers_id=info['id']).pack()))  
        
    kb = kb.adjust(2)
    
    kb.row(
        InlineKeyboardButton(text='< Назад', callback_data='back:Каталог')
    )
        
    return kb.as_markup()
    
    
def gen_menu_info_sneaker(key_brand: str, sneaker_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='В корзину', style='success', callback_data=RequestSneakerInCartCD(sneaker_id=sneaker_id, key_brand=key_brand).pack())],
        [InlineKeyboardButton(text='< Назад', callback_data=BrandCD(key_brand=key_brand).pack())]
    ])
    
    
def gen_menu_info_cart():
    kb = InlineKeyboardBuilder()
    
    for sneaker_id, info in CART:
        kb.row(InlineKeyboardButton(text=info['text'], callback_data=SneakersInCartCD(sneaker_id=sneaker_id).pack()))
    
    return kb.as_markup()
    
    
def gen_menu_info_sneaker_in_cart():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Купить', callback_data='pay')],
        [InlineKeyboardButton(text='< Назад', callback_data='back:Корзина')]
    ])
    