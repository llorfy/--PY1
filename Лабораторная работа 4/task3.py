def delete(list_, index=None): # TODO реализовать функцию удаления элемента из списка по индексу
    if index == None:
        index = len(list_)-1
    list_1 = list_[:index]
    list_2 = list_[index+1:]
    list_ = list_1 + list_2
    return list_

print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
