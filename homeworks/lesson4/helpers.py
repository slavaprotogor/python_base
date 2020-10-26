"""
Модуль с полезными функциями
"""
from time import time
from typing import Sequence, Iterable


def input_int(message: str) -> int:
    """
    Функция создает диалог ввода числа

    :param message: сообщение
    :return: число введенное пользователем
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Попробуйте еще раз')


def my_range(end: int = 0, start: int = 0, step: int = 1):
    """
    Генератор выдает последовательность чисел

    :param end: последний элемент
    :param start: начальный элемент
    :param step: шаг
    :return:
    """
    index = start
    while index <= end:
        yield index
        index += step
    else:
        raise StopIteration


def my_reduce(items: Sequence, func: callable, start: int = 0) -> float:
    """
    Применяет указанную функцию к элементам последовательности, сводя её к единственному значению

    :param items: последовательнсоть
    :param func: функция
    :param start: первый элемент
    :return: результат
    """
    result = start
    for item in items:
        result = func(item, result)
    return result


def my_cycle(items: Sequence, duration: int = 1):
    """
    Зацикленный вывод элементов последовательнсоти

    :param items: последовательность
    :param duration: продолжительность в секундах
    :return: элемент последовательности
    :param duration: продолжительность вывода в секундах
    """
    time_end = time() + duration
    index = 0
    while time() < time_end:
        try:
            yield items[index]
            index += 1
        except IndexError:
            index = 0
    else:
        raise StopIteration


def my_count(start: int = 0, step: int = 0, duration: int = 1):
    """
    Генерирует числа

    :param start: начальный элемент
    :param step: шаг
    :param duration: продолжительность вывода в секундах
    :return: элемент последовательности
    """
    time_end = time() + duration
    index = 0
    while time() < time_end:
        yield index
        index += step
    else:
        raise StopIteration


def my_enumerate(items: Iterable, start: int = 0):
    """
    Добавляет индекс при итерации

    :param items: последовательность
    :param start: начальное значение
    :return: элемент с индексом
    """
    index = start
    for item in items:
        yield index, item
        index += 1
