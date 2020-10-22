"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""
from helpers import input_type, my_pow


while True:
    digit_float = input_type('Действительное положительное число: ', check_type=float)
    if digit_float > 0:
        break
    print('Число должно быть положительным. Попробуйте еще раз.')

while True:
    digit_int = input_type('Целое отрицательно число: ', check_type=int)
    if digit_int < 0:
        break
    print('Число должно быть отрицательным. Попробуйте еще раз.')

result = my_pow(digit_float, digit_int)

print(f'Результат возведения числа {digit_float} в степень {digit_int} = ', result)
