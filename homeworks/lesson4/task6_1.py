"""
Итератор, генерирующий целые числа, начиная с указанного и до 10.
"""
import sys


if len(sys.argv) != 2:
    raise ValueError('Должен быть указан один параметр.')

try:
    start = int(sys.argv[1])
except ValueError:
    print('Параметр должен быть числовым')

for item in range(start, 11):
    print('Число: ', item)
