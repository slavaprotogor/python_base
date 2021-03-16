"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""
from typing import Union


class Complex:
    """ Класс комплексного числа """

    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """ Инициализация

        :param a: действительная часть
        :param b: мнимая часть
        """
        if not isinstance(a, (int, float)):
            raise TypeError('Arg "a" must be a digit')
        if not isinstance(b, (int, float)):
            raise TypeError('Arg "b" must be a digit')
        self.__a = a
        self.__b = b

    @property
    def a(self):
        """ Значение действительной части

        :return: действительная часть
        """
        return self.__a

    @property
    def b(self):
        """ Значение мнимая часть

        :return: мнимая часть
        """
        return self.__b

    def __add__(self, other):
        """ Сумма

        :param other: объект типа Complex
        :return: сумма
        """
        if not isinstance(other, Complex):
            raise TypeError('The object must be a Complex')

        return Complex(self.__a + other.a, self.__b + other.b)

    def __mul__(self, other):
        """ Умножение

        :param other: объект типа Complex
        :return: перемножение
        """
        if not isinstance(other, Complex):
            raise TypeError('The object must be a Complex')

        return Complex(self.__a * other.a - self.__b * other.b, self.__a * other.b + self.__b * other.a)

    def __str__(self):
        """ Строковое представление инстанаса Complex

        :return: str
        """
        b = f'+ i{self.__b}' if self.__b >= 0 else f'- i{abs(self.__b)}'
        return f'{self.__a} {b}'


if __name__ == '__main__':
    d1 = Complex(2, 3)
    print('Число 1: ', d1)
    d2 = Complex(-1, 1)
    print('Число 2: ', d2)
    d3 = d1 + d2
    print('Сумма = ', d3)
    d4 = d1 * d2
    print('Умножение = ', d4)
