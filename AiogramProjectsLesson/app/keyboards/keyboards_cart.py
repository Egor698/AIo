
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from data.cart_data import CART

from app.handlers.CallbackData import SneakerCartCD


#клавиатуры модуля cart
def gen_menu_sneakers_in_cart():
    kb = InlineKeyboardBuilder()
    
    for sneaker_id, text in CART.iter_sneaker_id_and_text_kb():
        kb.row(InlineKeyboardButton(text=text, callback_data=SneakerCartCD(sneaker_id=sneaker_id).pack()))
    
    return kb.as_markup()
    
    
def gen_menu_sneaker_in_cart():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Купить', style='success', callback_data='pay')],
        [InlineKeyboardButton(text='< Назад', callback_data='back:Корзина')]
    ])
    