"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
from helpers import input_type


def division(a: int, b: int) -> float:
    """
    Функция производит деление двух чисел

    :param a: первое число
    :param b: второе число
    :return: результат деления
    """
    return a / b


number1 = input_type('Введите целое число number1: ', check_type=int)
number2 = input_type('Введите целое число number2: ', check_type=int)

try:
    result = division(number1, number2)
    print(f'Результат деления num1 = {number1} и num2 = {number2} - ', result)
except ZeroDivisionError:
    print('На 0 делить нельзя')
