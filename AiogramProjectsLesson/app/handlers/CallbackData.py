from aiogram.filters.callback_data import CallbackData
from data.catalog_data import DataSneakers

class BrandCD(CallbackData, prefix='brand'):
    key_brand: str
    

class SneakerCD(CallbackData, prefix='sneakers'):
    key_brand: str
    sneaker_id: int
    
    
class RequestSneakerInCartCD(CallbackData, prefix='requestcart'):
    key_brand: str
    sneaker_id: int
    
    
class SneakerCartCD(CallbackData, prefix='sneakersincart'):
    sneaker_id: int