"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""
from helpers import my_range, my_reduce


print('Результат: ', my_reduce(my_range(1000, 100, 2), lambda x, y: x * y, 1))