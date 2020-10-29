"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
"""
from helpers import my_range


digits = [digit for digit in my_range(240, 20) if digit % 20 == 0 or digit % 21 == 0]

print('Результат: ', digits)
