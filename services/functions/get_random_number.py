from random import randint

def get_random_number():
    return "".join([str(randint(0, 9)) for i_ in range(8)])