import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';',
           ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`', '~']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_password():
    password_letters = random.randint(8, 10)
    password_symbols = random.randint(2, 4)
    password_numbers = random.randint(2, 4)

    letters_list = [str(random.choice(letters)) for nums in range(1, password_letters + 1)]
    symbols_list = [str(random.choice(symbols)) for nums in range(1, password_symbols + 1)]
    numbers_list = [str(random.choice(numbers)) for nums in range(1, password_numbers + 1)]

    passwords = letters_list + symbols_list + numbers_list

    random.shuffle(passwords)

    shuffled_password = ''.join(passwords)

    return shuffled_password
