"""
Модуль с полезными функциями
"""
import re
from typing import Sequence, Tuple


def input_int(message: str) -> int:
    """ Функция создает диалог ввода числа

    :param message: сообщение
    :return: число введенное пользователем
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Попробуйте еще раз')


def parse_to_int(text: str) -> int:
    """ Полчить число из строки или 0

    :param text: строка
    :return: число
    """
    return int(re.sub(r'\D', '', text) or 0)


def my_sum(items: Sequence) -> float:
    """ Функция возвращает сумму элементов в списке

    :param items: список элементов
    :return: сумма элементов
    """
    result = 0
    for item in items:
        result += item
    return result


def my_avg(items: Sequence) -> float:
    """ Функция считает среднее значение

    :param items: последовательность чисел
    :return: среднее значение
    """
    return my_sum(items) / len(items)


def my_map(func: callable, items: list) -> list:
    """
    Генератор вызывает функцию func для каждого элемента списка
    :param func: вызваемая функция
    :param items: список элементов
    :return: элемент
    """
    for item in items:
        yield func(item)


def file_stat(file_name: str) -> Tuple[int, int]:
    """ Считает количество строки и слов в файле

    :param file_name: полное имя файла
    :return: кол-во строк, кол-во слов
    """
    l_count, w_count = 0, 0
    with open(file_name, 'r') as f:
        for line in f:
            l_count += 1
            w_count += len(line.split())
    return l_count, w_count
