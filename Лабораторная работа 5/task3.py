import random
def get_unique_list_numbers() -> list[int]:
    n = 15
    list_ = random.sample(range(-10, 10), n)  # TODO написать функцию для получения списка уникальных целых чисел
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
