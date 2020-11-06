"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""
from helpers import input_type, my_sorted, my_sum


def sum_numbers(a: int, b: int, c: int) -> list:
    """
    Возвращает сумму двух самых больших чисел

    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: сумма двух самых больших чисел
    """
    return my_sum(my_sorted([a, b, c], reverse=True)[:2])


number1 = input_type('Ввеите первое число: ', check_type=int)
number2 = input_type('Ввеите второе число: ', check_type=int)
number3 = input_type('Ввеите третье число: ', check_type=int)

result = sum_numbers(number1, number2, number3)

print('Сумма двух самых больших чисел = ', result)
