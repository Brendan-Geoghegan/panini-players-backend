import string
import random


def id_generator():
    letters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(letters) for i in range(10))
    return id


def rarity_calculator(sticker):
    if sticker['price'] == "£0.29":
        rarity = 1
    elif sticker['price'] == "£0.35":
        rarity = 2
    elif sticker['price'] == "£0.59":
        rarity = 3
    elif sticker['price'] == "£0.65" or sticker['price'] == "£0.69" or sticker['price'] == "£0.75":
        rarity = 4
    else:
        rarity = 5
    return rarity
