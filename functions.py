import random
from os import remove

DECK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A','A','A','A', 'J', 'Q', 'K']

def deal_random_card():
    return random.choice(DECK)

def picture_to_number_list(x):
    y = []
    for item in x:
        if item == 'A':
            y.append(11)

        elif item == 'K' or item == 'Q' or item == 'J':
            y.append(10)
        else:
            y.append(int(item))

    return y



def check_bust (x):
    if x > 21:
        return True
    else:
        return False

def check_blackjack (x):
    if x == 21:
        return True
    else:
        return False