# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

n = 15
list_d = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(n+1)]
pprint(list_d)