"""
Модуль содержит набор полезных функций
"""


def input_type(message: str, check_type) -> int:
    """
    Функция создает диалог ввода числа заданного типа

    :param message: сообщение
    :param check_type: проверяемый тип
    :return: число введенное пользователем
    """
    while True:
        try:
            return check_type(input(message))
        except ValueError:
            print('Попробуйте еще раз')


def my_sorted(items: list, reverse: bool = False) -> list:
    """
    Функция возвращает отсортированный массив

    :param items: список элементов
    :param reverse: сортровать в обратном порядке
    :return: отсортированный список
    """
    return sorted(items, reverse=True)


def my_sum(items: list) -> float:
    """
    Функция возвращает сумму элементов в списке

    :param items: список элементов
    :return: сумма элементов
    """
    result = 0
    for item in items:
        result += item
    return result


def my_pow(base: float, exp: float) -> float:
    """
    Функция возводит в степень число

    :param base: число
    :param exp: степень
    :return: возведенное в степень число
    """
    return pow(base, exp)


def my_map(func: callable, items: list) -> list:
    """
    Генератор вызывает функцию func для каждого элемента списка

    :param func: вызваемая функция
    :param items: список элементов
    :return: элемент
    """
    for item in items:
        yield func(item)


def my_capitalize(text: str) -> str:
    """
    Функция возвращает строку с заглавной буквой

    :param text: строка
    :return: строка с заглавной буквой
    """
    return text[0].upper() + text[1:].lower()
