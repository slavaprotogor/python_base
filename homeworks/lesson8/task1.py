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

    def __init__(self, date_str: str):
        self._date_str = date_str

    @classmethod
    def date_to_int(cls, date_str: str) -> Tuple[int, int, int]:
        if not cls.is_valid_date(date_str):
            raise ValueError('The date is incorrect')
        day, month, year = tuple(map(int, date_str.split('-')))
        return day, month, year

    @staticmethod
    def is_valid_date(date_str: str) -> bool:
        date_parse = re.match(r'^([1-3]?\d)-(1?\d)-(\d{4})$', date_str)

        if not date_parse:
            return False

        day_parse = int(date_parse.group(1))
        if day_parse == 0 or day_parse > 31:
            return False

        month_parse = int(date_parse.group(2))
        if month_parse == 0 or month_parse > 12:
            return False

        return True


if __name__ == '__main__':
    assert Date.date_to_int('30-12-5232') == (30, 12, 5232), 'Error'
    assert Date.date_to_int('22-11-2002') == (22, 11, 2002), 'Error'
