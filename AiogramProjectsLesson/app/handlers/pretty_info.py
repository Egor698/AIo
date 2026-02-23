from data.catalog_data import CATALOG, DataSneakers
from data.cart_data import CART

def get_pretty_text_and_photo(sneaker_data: DataSneakers) -> tuple[str, str]:
    
    formatted_price = f"{sneaker_data.price:,}".replace(',', ' ')
    
    text = f"""👟 <b>{sneaker_data.name}</b>
💰 <b>Цена:</b> {formatted_price} ₽
📝 <b>Описание:</b>
{sneaker_data.description}
"""
    return text, sneaker_data.photo_url


def get_info_about_sneaker_catalog(key_brand: str, sneaker_id: str) -> tuple[str, str]:
    
    sneaker_data = CATALOG.search_sneaker_data(key_brand, sneaker_id)

    return get_pretty_text_and_photo(sneaker_data)
    
    
def get_info_about_sneaker_in_cart(sneaker_id: int) -> tuple[str, str]:
    sneaker_data = CART.search_sneaker_data(sneaker_id)
    
    return get_pretty_text_and_photo(sneaker_data)
    
    
            