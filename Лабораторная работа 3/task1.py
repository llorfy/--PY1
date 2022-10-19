src = not False and True or False and not True

# result = True and True or False and False (избавились от "not")
# result = True or False (избавились от "and")
# result = True (избавились от "or")

result = True  # TODO подставить результат выражения

print(src == result)
