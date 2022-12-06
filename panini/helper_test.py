from .helper import id_generator, rarity_calculator

def test_id_generator(api):
    assert len(id_generator()) == 10


def test_rarity_calculator(api):
    assert rarity_calculator({
        "index": 0,
        "sticker_code": "00",
        "sticker_name": "Panini Logo",
        "image": "cdn.shopify.com/s/files/1/0561/4639/5336/products/IMG_1761@2x.jpg",
        "price": "£0.99"
    }) == 5


# def test_add_sticker(api):
#     pass


# def test_remove_sticker(api):
#     pass
