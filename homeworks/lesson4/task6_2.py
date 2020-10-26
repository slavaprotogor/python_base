"""
Итератор, повторяющий элементы некоторого списка, определенного заранее с ограниченным количеством вывода.
"""
import sys
from itertools import cycle


if len(sys.argv) != 2:
    raise ValueError('Должен быть указан один параметр.')

try:
    number = int(sys.argv[1])
except ValueError:
    print('Параметр должен быть числовым')

for index, item in enumerate(cycle('ABCD')):
    if index == number:
        break
    print('Элемент: ', item)
