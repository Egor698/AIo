from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters.callback_data import CallbackData
from app.handlers.CallbackData import RequestSneakerInCartCD, SneakerCartCD
import app.keyboards.keyboards_cart as kb_cart
import app.handlers.pretty_info as pi
from data.cart_data import CART

router = Router()

@router.callback_query(RequestSneakerInCartCD.filter())
async def cmd_add_in_cart(queru: CallbackQuery, callback_data: RequestSneakerInCartCD):
    result = CART.add_sneaker_in_cart_and_return_success(callback_data.key_brand,
                                                          callback_data.sneaker_id)
    
    if result:
        await queru.answer('Товар добавлен в корзину!', show_alert=True)
    else:
        await queru.answer('Товар уже в корзине!', show_alert=True)


@router.callback_query(F.data=="back:Корзина")
@router.message(F.text=="Корзина")
async def cmd_info_sneakers_in_cart(update: Message | CallbackQuery):
    if isinstance(update, CallbackQuery):
        
        await update.answer('')
        await update.message.delete()
        
        await update.message.answer(
            text='Ваша корзина',
            reply_markup=kb_cart.gen_menu_sneakers_in_cart()
        )
    else:
        await update.answer(
            text='Ваша корзина',
            reply_markup=kb_cart.gen_menu_sneakers_in_cart()
        )

    
@router.callback_query(SneakerCartCD.filter())
async def cmd_info_sneaker_in_cart(queru: CallbackQuery, callback_data: SneakerCartCD):
    
    await queru.answer('')
    await queru.message.delete()
    
    caption, photo_url = pi.get_info_about_sneaker_in_cart(callback_data.sneaker_id)
    
    await queru.message.answer_photo(caption=caption,
                                photo=photo_url,
                                parse_mode="HTML",
                                reply_markup=kb_cart.gen_menu_sneaker_in_cart())
    