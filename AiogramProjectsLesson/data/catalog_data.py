from dataclasses import dataclass, field
from typing import Iterator

@dataclass
class DataSneakers:
    id: int
    price: int
    name: str
    description: str
    photo_url: str = field(default='https://avatars.mds.yandex.net/i?id=d0356ef660146519a73f85288a60c79e_l-8995617-images-thumbs&n=13')


CATALOG_TABLE = {
            'nike': {
                'text': 'Nike',
                'items': {
                    1: {'text': 'Air Max 90', 'data': DataSneakers(
                        id=1,
                        photo_url='https://cdn1.ozone.ru/s3/multimedia-x/6889698429.jpg',
                        price=12500,
                        name='Nike Air Max 90',
                        description='Классические кроссовки с воздушной подушкой'
                    )},
                    2: {'text': 'Air Force 1', 'data': DataSneakers(
                        id=2,
                        photo_url='https://avatars.mds.yandex.net/get-mpic/1853752/2a00000197a6a7d631a28588abc19132afac/optimize',
                        price=11000,
                        name='Nike Air Force 1',
                        description='Легендарные кроссовки, икона уличной моды'
                    )},
                    3: {'text': 'Air Jordan 1', 'data': DataSneakers(
                        id=3,
                        photo_url='https://ir.ozone.ru/s3/multimedia-1-t/8548239089.jpg',
                        price=18900,
                        name='Air Jordan 1',
                        description='Баскетбольная классика от Майкла Джордана'
                    )},
                    4: {'text': 'Dunk Low', 'data': DataSneakers(
                        id=4,
                        photo_url='https://avatars.mds.yandex.net/get-mpic/18252787/2a00000199a92c1eefab6c9145494921d347/orig',
                        price=15700,
                        name='Nike Dunk Low',
                        description='Скейтерская классика в повседневном стиле'
                    )},
                    5: {'text': 'Air Max 270', 'data': DataSneakers(
                        id=5,
                        photo_url='https://main-cdn.sbermegamarket.ru/big1/hlr-system/ccs/256944/NTE3MTk5XzU4MDcxMDk5/b0.jpeg',
                        price=14500,
                        name='Nike Air Max 270',
                        description='Максимальная амортизация для комфорта'
                    )},
                }
            },
            'adidas': {
                'text': 'Adidas',
                'items': {
                    6: {'text': 'Ultraboost 22', 'data': DataSneakers(
                        id=6,
                        price=16900,
                        name='Adidas Ultraboost 22',
                        description='Лучшие беговые кроссовки с энергоемкой подошвой'
                    )},
                    7: {'text': 'NMD R1', 'data': DataSneakers(
                        id=7,
                        price=14700,
                        name='Adidas NMD R1',
                        description='Урбанистический стиль с блоками на подошве'
                    )},
                    8: {'text': 'Superstar', 'data': DataSneakers(
                        id=8,
                        price=9900,
                        name='Adidas Superstar',
                        description='Вечная классика с ракушкой на носке'
                    )},
                    9: {'text': 'Stan Smith', 'data': DataSneakers(
                        id=9,
                        price=8900,
                        name='Adidas Stan Smith',
                        description='Минималистичные теннисные кроссовки'
                    )},
                    10: {'text': 'Yeezy 350', 'data': DataSneakers(
                        id=10,
                        price=32900,
                        name='Adidas Yeezy 350',
                        description='Коллаборация с Канье Уэстом'
                    )},
                }
            },
            'new_balance': {
                'text': 'New Balance',
                'items': {
                    11: {'text': '574', 'data': DataSneakers(
                        id=11,
                        price=9900,
                        name='New Balance 574',
                        description='Классическая модель на каждый день'
                    )},
                    12: {'text': '990v5', 'data': DataSneakers(
                        id=12,
                        price=18900,
                        name='New Balance 990v5',
                        description='Премиальная модель made in USA'
                    )},
                    13: {'text': '327', 'data': DataSneakers(
                        id=13,
                        price=11200,
                        name='New Balance 327',
                        description='Ретро-стиль с массивной подошвой'
                    )},
                    14: {'text': '2002R', 'data': DataSneakers(
                        id=14,
                        price=14500,
                        name='New Balance 2002R',
                        description='Комфорт и стиль в каждой детали'
                    )},
                    15: {'text': '5740', 'data': DataSneakers(
                        id=15,
                        price=12500,
                        name='New Balance 5740',
                        description='Современная интерпретация классики'
                    )},
                }
            },
            'puma': {
                'text': 'Puma',
                'items': {
                    16: {'text': 'Suede', 'data': DataSneakers(
                        id=16,
                        price=6900,
                        name='Puma Suede',
                        description='Легендарные замшевые кроссовки'
                    )},
                    17: {'text': 'RS-X', 'data': DataSneakers(
                        id=17,
                        price=11900,
                        name='Puma RS-X',
                        description='Массивный дизайн с яркими цветами'
                    )},
                    18: {'text': 'Cali', 'data': DataSneakers(
                        id=18,
                        price=8900,
                        name='Puma Cali',
                        description='Калифорнийский стиль 80-х'
                    )},
                    19: {'text': 'Future Rider', 'data': DataSneakers(
                        id=19,
                        price=7900,
                        name='Puma Future Rider',
                        description='Легкие кроссовки для активного дня'
                    )},
                    20: {'text': 'Smash v2', 'data': DataSneakers(
                        id=20,
                        price=5900,
                        name='Puma Smash v2',
                        description='Теннисная классика на каждый день'
                    )},
                }
            },
            'reebok': {
                'text': 'Reebok',
                'items': {
                    21: {'text': 'Club C 85', 'data': DataSneakers(
                        id=21,
                        price=7900,
                        name='Reebok Club C 85',
                        description='Теннисная классика 80-х'
                    )},
                    22: {'text': 'Classic Leather', 'data': DataSneakers(
                        id=22,
                        price=6900,
                        name='Reebok Classic Leather',
                        description='Вечная классика из кожи'
                    )},
                    23: {'text': 'Royal Glide', 'data': DataSneakers(
                        id=23,
                        price=5900,
                        name='Reebok Royal Glide',
                        description='Мягкие и удобные кроссовки'
                    )},
                    24: {'text': 'Zig Kinetica', 'data': DataSneakers(
                        id=24,
                        price=12900,
                        name='Reebok Zig Kinetica',
                        description='Инновационная зигзагообразная подошва'
                    )},
                    25: {'text': 'Nano X2', 'data': DataSneakers(
                        id=25,
                        price=11900,
                        name='Reebok Nano X2',
                        description='Для кроссфита и тренировок'
                    )},
                }
            },
            'asics': {
                'text': 'Asics',
                'items': {
                    26: {'text': 'Gel-Kayano 29', 'data': DataSneakers(
                        id=26,
                        price=15900,
                        name='Asics Gel-Kayano 29',
                        description='Стабильность для бега'
                    )},
                    27: {'text': 'Gel-Nimbus 25', 'data': DataSneakers(
                        id=27,
                        price=16500,
                        name='Asics Gel-Nimbus 25',
                        description='Максимальная амортизация'
                    )},
                    28: {'text': 'Gel-Quantum 180', 'data': DataSneakers(
                        id=28,
                        price=11900,
                        name='Asics Gel-Quantum 180',
                        description='Современный дизайн для города'
                    )},
                    29: {'text': 'Gel-Cumulus 25', 'data': DataSneakers(
                        id=29,
                        price=13500,
                        name='Asics Gel-Cumulus 25',
                        description='Универсальные беговые кроссовки'
                    )},
                    30: {'text': 'Gel-Excite 9', 'data': DataSneakers(
                        id=30,
                        price=7900,
                        name='Asics Gel-Excite 9',
                        description='Бюджетные беговые кроссовки'
                    )},
                }
            },
            'converse': {
                'text': 'Converse',
                'items': {
                    31: {'text': 'Chuck 70', 'data': DataSneakers(
                        id=31,
                        price=8900,
                        name='Converse Chuck 70',
                        description='Премиальная версия классики'
                    )},
                    32: {'text': 'Chuck Taylor', 'data': DataSneakers(
                        id=32,
                        price=6900,
                        name='Converse Chuck Taylor',
                        description='Легендарные кеды на каждый день'
                    )},
                    33: {'text': 'Run Star Hike', 'data': DataSneakers(
                        id=33,
                        price=11900,
                        name='Converse Run Star Hike',
                        description='Кеды с массивной подошвой'
                    )},
                    34: {'text': 'One Star', 'data': DataSneakers(
                        id=34,
                        price=7900,
                        name='Converse One Star',
                        description='Классические низкие кеды со звездой'
                    )},
                    35: {'text': 'Weapon CX', 'data': DataSneakers(
                        id=35,
                        price=9900,
                        name='Converse Weapon CX',
                        description='Баскетбольный стиль 80-х'
                    )},
                }
            },
            'vans': {
                'text': 'Vans',
                'items': {
                    36: {'text': 'Old Skool', 'data': DataSneakers(
                        id=36,
                        price=6900,
                        name='Vans Old Skool',
                        description='Культовые скейтерские кеды'
                    )},
                    37: {'text': 'Sk8-Hi', 'data': DataSneakers(
                        id=37,
                        price=7900,
                        name='Vans Sk8-Hi',
                        description='Высокие скейтерские кеды'
                    )},
                    38: {'text': 'Authentic', 'data': DataSneakers(
                        id=38,
                        price=5900,
                        name='Vans Authentic',
                        description='Оригинальные кеды Vans'
                    )},
                    39: {'text': 'Era', 'data': DataSneakers(
                        id=39,
                        price=6200,
                        name='Vans Era',
                        description='Улучшенная версия Authentic'
                    )},
                    40: {'text': 'Slip-On', 'data': DataSneakers(
                        id=40,
                        price=6400,
                        name='Vans Slip-On',
                        description='Кеды без шнурков'
                    )},
                }
            },
            'saucony': {
                'text': 'Saucony',
                'items': {
                    41: {'text': 'Jazz Original', 'data': DataSneakers(
                        id=41,
                        price=8900,
                        name='Saucony Jazz Original',
                        description='Винтажные беговые кроссовки'
                    )},
                    42: {'text': 'Shadow 5000', 'data': DataSneakers(
                        id=42,
                        price=12900,
                        name='Saucony Shadow 5000',
                        description='Классика беговой культуры'
                    )},
                    43: {'text': 'Grid 8000', 'data': DataSneakers(
                        id=43,
                        price=11900,
                        name='Saucony Grid 8000',
                        description='Ретро-модель с сеткой'
                    )},
                    44: {'text': 'Shadow 6000', 'data': DataSneakers(
                        id=44,
                        price=13500,
                        name='Saucony Shadow 6000',
                        description='Премиальная ретро-модель'
                    )},
                    45: {'text': 'Azura', 'data': DataSneakers(
                        id=45,
                        price=9900,
                        name='Saucony Azura',
                        description='Яркий дизайн 90-х'
                    )},
                }
            },
            'mizuno': {
                'text': 'Mizuno',
                'items': {
                    46: {'text': 'Wave Rider 26', 'data': DataSneakers(
                        id=46,
                        price=13900,
                        name='Mizuno Wave Rider 26',
                        description='Японское качество для бега'
                    )},
                    47: {'text': 'Wave Prophecy X', 'data': DataSneakers(
                        id=47,
                        price=18900,
                        name='Mizuno Wave Prophecy X',
                        description='Футуристический дизайн'
                    )},
                    48: {'text': 'Wave Inspire 18', 'data': DataSneakers(
                        id=48,
                        price=12500,
                        name='Mizuno Wave Inspire 18',
                        description='Поддержка для бега'
                    )},
                    49: {'text': 'Wave Horizon 5', 'data': DataSneakers(
                        id=49,
                        price=15900,
                        name='Mizuno Wave Horizon 5',
                        description='Максимальная стабильность'
                    )},
                    50: {'text': 'Wave Creation 23', 'data': DataSneakers(
                        id=50,
                        price=16900,
                        name='Mizuno Wave Creation 23',
                        description='Для бега с нейтральной пронацией'
                    )},
                }
            }
        }

     
class Catalog:
    def __init__(self):
        self._catalog = CATALOG_TABLE
    
    def search_sneaker_data(self, key_brand: str, sneaker_id: int) -> DataSneakers:
        if key_brand not in self._catalog:
            raise KeyError('Ключ бренда не найден в каталоге')
        
        if sneaker_id not in self._catalog[key_brand]['items']:
            raise KeyError('Id кроссовка не найден в каталоге')
        
        return self._catalog[key_brand]['items'][sneaker_id]['data']
    
    
    def iter_sneaker_id_and_text_kb(self, key_brand: str) -> Iterator[tuple]:
        if key_brand not in self._catalog:
            raise KeyError('Ключ бренда не найден в каталоге')
        
        return ((sneaker_id, info['text'])
                for sneaker_id, info in self._catalog[key_brand]['items'].items())
    

    def iter_key_brand_and_text_kb(self) -> Iterator[tuple]:
        return ((key_brand, info['text'])
                for key_brand, info in self._catalog.items())
        
        
CATALOG = Catalog()