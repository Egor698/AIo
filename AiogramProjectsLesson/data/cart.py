from data.catalog import CATALOG, DataSneakers

class Cart:
    def __init__(self):
        self.cart = {}
        
    def add_sneakers_in_cart_and_return_success(self, key_brand: str, sneakers_id: int) -> bool:
        sneakers_data = self.search_sneakers_data(key_brand, sneakers_id)
        
        if sneakers_id not in self.cart:
            self.cart.update({sneakers_id: {'text': sneakers_data.name, 'data': sneakers_data}})
            return True
        else:
            return False
            
        
    def search_sneakers_data(self, key_brand: str, sneakers_id: int) -> DataSneakers:
        sneakers_data = None
    
        for sneakers_info in CATALOG[key_brand]['items']:
            if sneakers_info['id'] == sneakers_id:
                sneakers_data = sneakers_info['data']
                break
            
        if not sneakers_data:
            raise ValueError(f'Кроссовок с id {sneakers_id} не найден для корзины')
        
        return sneakers_data
    
    
    def __iter__(self):
        for sneakers_id, info in self.cart.items():
            yield (sneakers_id, info)
        
        
    def search_sneaker_info_in_cart(self, sneakers_id: int) -> DataSneakers:
        sneakers_data = self.cart.get(sneakers_id)
            
        if not sneakers_data:
            raise ValueError(f'Кроссовок с id {sneakers_id} не найден для корзины')
        
        return sneakers_data['data']


CART = Cart()