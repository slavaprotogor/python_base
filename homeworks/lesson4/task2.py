"""
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""
from typing import Sequence


def digits_new(digits: Sequence):
    """
    Выдает числа, которые больше предыдущего в последовательности

    :param digits:
    :return: число
    """
    i = 1
    while True:
        try:
            if digits[i] > digits[i - 1]:
                yield digits[i]
            i += 1
        except IndexError:
            raise StopIteration


digit_list = (8, 7, 3, 63, 5, 5, 7, 8)

print('Новый список: ', list(digits_new(digit_list)))
