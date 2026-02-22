from aiogram.filters.callback_data import CallbackData
from data.catalog import DataSneakers

class BrandCD(CallbackData, prefix='brand'):
    key_brand: str
    

class SneakersCD(CallbackData, prefix='sneakers'):
    key_brand: str
    sneakers_id: int
    
    
class RequestSneakerInCartCD(CallbackData, prefix='requestcart'):
    key_brand: str
    sneaker_id: int
    
class SneakersInCartCD(CallbackData, prefix='sneakersincart'):
    sneaker_id: int