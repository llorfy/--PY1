def get_count_char(str_):     # TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_ = {}
    str_ = str_.lower()
    for i in range(len(str_)):      # сначала я создаю словарь с нулями (иначе у меня не работало)
        symbol_ = str_[i:i+1]
        if symbol_.isalpha():
            dict_[symbol_] = 0

    for i in range(len(str_)):      # здесь записываю количество каждого символа в строке
        symbol_ = str_[i:i+1]
        if symbol_.isalpha():
            dict_[symbol_] = int(dict_[symbol_]) + 1
    return dict_

def percent_char(dict_):            # это функция процентного отношения символов
    per = sum(dict_.values()) / 100
    for i, count in dict_.items():
        dict_[i] = str(round(float(dict_[i]) / per, 1)) + '%'
    return dict_

#main_str = "абвгд абвг абв l"
main_str = """
    Данное предложение будет разбиваться на отдельные слова.
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов.
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent_char(get_count_char(main_str)))
