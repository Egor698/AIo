from data.catalog_data import CATALOG, DataSneakers
from typing import Iterator

CART_TABLE = {}

class Cart:
    def __init__(self):
        self._cart = CART_TABLE
        
    def add_sneaker_in_cart_and_return_success(self, key_brand: str, sneaker_id: int) -> bool:
        sneaker_data = CATALOG.search_sneaker_data(key_brand, sneaker_id)
        
        if sneaker_data.id not in self._cart:
            self._cart.update({sneaker_data.id: sneaker_data})
            return True
        else:
            return False
            
        
    def search_sneaker_data(self, sneaker_id: int) -> DataSneakers:
        sneaker_data = self._cart.get(sneaker_id)
            
        if not sneaker_data:
            raise ValueError(f'Кроссовок с id {sneaker_id} не найден для корзины')
        
        return sneaker_data


    def iter_sneaker_id_and_text_kb(self) -> Iterator[tuple]:
        return ((sneaker_id, sneaker_data.name)
                for sneaker_id, sneaker_data in self._cart.items())

    
CART = Cart()