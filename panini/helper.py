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
            # add conditionals here for cases where ECU1 and ECU10
            index = cards_array.index(card)
            unique = card
    [code , num] = unique.split('-')
    added = int(num) + 1
    cards_array[index] = f"{code}-{added}"
    return ' '.join(cards_array)

def remove_sticker(cards, input_code):
    #need to add conditional for when the user only has 1 sticker left
    cards_array = cards.split(' ')
    for card in cards_array:
        if str.__contains__(card, input_code):
            # add conditionals here for cases where ECU1 and ECU10
            index = cards_array.index(card)
            unique = card
    [code , num] = unique.split('-')
    added = int(num) - 1
    cards_array[index] = f"{code}-{added}"
    return ' '.join(cards_array)
