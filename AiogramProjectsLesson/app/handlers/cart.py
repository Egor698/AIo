from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from app.handlers.CallbackData import RequestSneakerInCartCD, SneakersInCartCD
import app.keyboards as kb
import app.handlers.pretty_info as pi
from data.cart import CART

router = Router()

@router.callback_query(RequestSneakerInCartCD.filter())
async def add_in_cart(queru: CallbackQuery, callback_data: RequestSneakerInCartCD):
    result = CART.add_sneakers_in_cart_and_return_success(callback_data.key_brand,
                                                          callback_data.sneaker_id)
    
    if result:
        await queru.answer('Товар добавлен в корзину!', show_alert=True)
    else:
        await queru.answer('Товар уже в корзине!', show_alert=True)


@router.message(F.text=='Корзина')
async def cmd_info_cart(msg: Message):
    
    await msg.answer(text='Ваша корзина',
                     reply_markup=kb.gen_menu_info_cart())
    
    
@router.callback_query(F.data=="back:Корзина")
@router.message(F.text=="Каталог")
async def cmd_info_brand(update: Message | CallbackQuery):
    if isinstance(update, CallbackQuery):
        
        await update.answer('')
        await update.message.delete()
        
        await update.message.answer(
            text='Ваша корзина',
            reply_markup=kb.gen_menu_info_cart()
        )
    else:
        await update.answer(
            text='Ваша корзина',
            reply_markup=kb.gen_menu_info_cart()
        )

    
    
@router.callback_query(SneakersInCartCD.filter())
async def cmd_info_sneakers_in_cart(queru: CallbackQuery, callback_data: SneakersInCartCD):
    
    await queru.answer('')
    await queru.message.delete()
    
    caption, photo_url = pi.get_info_cart_about_sneaker(callback_data.sneaker_id)
    
    await queru.message.answer_photo(caption=caption,
                                photo=photo_url,
                                parse_mode="HTML",
                                reply_markup=kb.gen_menu_info_sneaker_in_cart())
    