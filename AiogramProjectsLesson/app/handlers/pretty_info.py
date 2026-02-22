from data.catalog import CATALOG
from data.cart import CART

def get_info_and_photo_about_sneaker(key_brand: str, sneakers_id: str) -> tuple[str, str]:
    #получаем класс DataSneakers в CATALOG
    sneakers_data = None
    
    for sneakers_info in CATALOG[key_brand]['items']:
        if sneakers_info['id'] == sneakers_id:
            sneakers_data = sneakers_info['data']
            break
        
    if not sneakers_data:
        raise ValueError('Кроссовок не найден')
    
    #делаем красивый вывод
    formatted_price = f"{sneakers_data.price:,}".replace(',', ' ')
    
    text = f"""👟 <b>{sneakers_data.name}</b>
💰 <b>Цена:</b> {formatted_price} ₽
📝 <b>Описание:</b>
{sneakers_data.description}
"""
    return text, sneakers_data.photo_url
    
    
def get_info_cart_about_sneaker(sneakers_id: int) -> tuple[str, str]:
    sneakers_data = CART.search_sneaker_info_in_cart(sneakers_id)
    
    formatted_price = f"{sneakers_data.price:,}".replace(',', ' ')
    
    text = f"""👟 <b>{sneakers_data.name}</b>
💰 <b>Цена:</b> {formatted_price} ₽
📝 <b>Описание:</b>
{sneakers_data.description}
"""
    return text, sneakers_data.photo_url
    
    
            