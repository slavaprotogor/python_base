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


def my_sorted(elements: list, reverse: bool = False) -> list:
    """
    Функция возвращает отсортированный массив.
    Используется алгоритм "Быстрая сортировка".

    :param elements: список элементов
    :param reverse: сортровать в обратном порядке
    :return: отсортированный список
    """

    def partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while reverse and nums[i] > pivot or \
                    not reverse and nums[i] < pivot:
                i += 1

            j -= 1
            while reverse and nums[j] < pivot or \
                    not reverse and nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

    def quick_sort(nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

    quick_sort(elements)
    return elements


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
    if exp == 0:
        return 1
    if exp == -1:
        return 1. / base
    result = my_pow(base, exp // 2)
    result *= result
    if exp % 2:
        result *= base
    return result


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


def is_latin_lower(text: str) -> bool:
    """
    Функция проверяет состоит ли текст лько из латинских букв нижнего регистра

    :param text: текст
    :return: True/False
    """
    return all((97 <= ord(char) <= 122 for char in text))
