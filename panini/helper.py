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


def add_sticker(cards, input_code):
    cards_array = cards.split(' ')
    for card in cards_array:
        if str.__contains__(card, input_code):
            unique = card
            [code, num] = unique.split('-')
            print('###########')
            index = cards_array.index(card)
            if len(code) == 4:
                break
    print('**********************')
    added = int(num) + 1
    cards_array[index] = f"{code}-{added}"
    return ' '.join(cards_array)


def remove_sticker(cards, input_code):
    cards_array = cards.split(' ')
    try:
        for card in cards_array:
            if str.__contains__(card, input_code):
                index = cards_array.index(card)
                unique = card
                [code, num] = unique.split('-')
                if int(num) <= 1:
                    raise Exception
                if len(code) == 4:
                    break
        added = int(num) - 1
        cards_array[index] = f"{code}-{added}"
        return ' '.join(cards_array)
    except Exception:
        print("you dont have enough stickers")
        return cards
