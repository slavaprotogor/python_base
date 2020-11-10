"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import re
from typing import Tuple


class Date:
    """ Класс даты """

    def __init__(self, date_str: str):
        """ Инициализация

        :param date_str: строковое представление даты
        """
        self._date_str = date_str

    @classmethod
    def date_to_int(cls, date_str: str) -> Tuple[int, int, int]:
        """ Конвертирует строковое предстваление даты в кортеж

        :param date_str: строковое предстваление даты
        :return: кортеж
        """
        if not cls.is_valid_date(date_str):
            raise ValueError('The date is incorrect')
        day, month, year = tuple(map(int, date_str.split('-')))
        return day, month, year

    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        """ Проверка валидности даты

        :param date_str: строковое предстваление даты
        :return: bool
        """
        date_parse = re.match(r'^([1-9]|[12]\d|3[01])-([1-9]|1[0-2])-(\d{4})$', date_str)

        if not date_parse:
            return False

        return True


if __name__ == '__main__':
    assert Date.date_to_int('31-12-5232') == (31, 12, 5232), 'Error'
    assert Date.date_to_int('2-11-2002') == (2, 11, 2002), 'Error'
