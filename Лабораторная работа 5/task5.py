import random
import string
def get_random_password() -> str:
    n = 8
    lots = string.ascii_letters + string.digits
    password = ''.join(random.sample(lots, n))
    return password
    # TODO написать функцию генерации случайных паролей

print(get_random_password())
