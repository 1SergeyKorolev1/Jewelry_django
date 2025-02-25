from random import randint

def get_random_number():
    return "".join([str(randint(0, 15)) for i_ in range(14)])