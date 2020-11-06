"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""
from typing import List


class Matrix:
    """ Класс матрицы """
    def __init__(self, items: List[List[float or int]]):
        """ Инициализация инстанса класса

        :param items: список списков с числами
        """
        if not isinstance(items, list) or not isinstance(items[0], list):
            raise TypeError('Items must be a list of list digits')

        self.__items = items

    @property
    def row_count(self) -> int:
        """ Свойство возвращает количество строк матрицы

        :return: количество строк
        """
        return len(self.__items)

    @property
    def column_count(self) -> int:
        """ Свойство возвращает количество столбцов матрицы

        :return: количество столбцов
        """
        return len(self.__items[0])

    @property
    def items(self) -> List[List[float or int]]:
        """ Свойство возвращает список списков

        :return: список списков
        """
        return self.__items

    def __str__(self) -> str:
        """ Строковое представление матрицы """

        values_str = ''
        for row in self.__items:
            values_str += ', '.join(map(str, row)) + '\n'
        return values_str

    def __add__(self, other):
        """ Сложение матрицы

        :param other: объект Matrix
        :return: новая матрица
        """
        if not isinstance(other, Matrix):
            raise TypeError('The object must be a Matrix')

        if self.row_count != other.row_count or self.row_count != other.row_count:
            raise ValueError('Matrices must be equal size')

        items_new = []
        for row in range(self.row_count):
            row_new = [] 
            for column in range(self.column_count):
                row_new.append(self.items[row][column] + other.items[row][column])
            items_new.append(row_new)

        return Matrix(items_new)


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('Matrix 1:')
    print(m1)

    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('Matrix 2:')
    print(m2)

    print('Matrix sum:')
    print(m1 + m2)
