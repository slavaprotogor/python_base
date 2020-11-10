"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise TypeError('The object must be a Complex')

        return Complex(self.__a + other.a, self.__b + other.b)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise TypeError('The object must be a Complex')

        return Complex(self.__a * other.a - self.__b * other.b, self.__a * other.b + self.__b * other.a)

    def __str__(self):
        b = f'+ {self.__b}' if self.__b >= 0 else f'- {abs(self.__b)}'
        return f'{self.__a} {b}i'


if __name__ == '__main__':
    d1 = Complex(2, 3)
    print('Число 1: ', d1)
    d2 = Complex(-1, 1)
    print('Число 2: ', d2)
    d3 = d1 + d2
    print('Сумма = ', d3)
    d4 = d1 * d2
    print('Умножение = ', d4)


