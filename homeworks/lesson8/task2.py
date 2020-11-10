"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


def input_float(message: str) -> float:
    """ Диалог ввода чисел

    :param message: сообщение
    :return:
    """
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print('Значение должно быть числовым')
            continue
        return value


class MyZeroDivisionError(ZeroDivisionError):
    pass


class Digit:

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be a digit')
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return str(self.__value)

    def __truediv__(self, other):
        if not isinstance(other, Digit):
            raise TypeError('Value must be a digit')

        if other.value == 0:
            raise MyZeroDivisionError('division by zero')

        return Digit(self.value / other.value)


if __name__ == '__main__':
    while True:
        d1 = Digit(input_float('Введите первое число: '))
        d2 = Digit(input_float('Введите второе число: '))
        print(f'Деление {d1} на {d2}: ')
        try:
            d3 = d1 / d2
        except MyZeroDivisionError:
            print('Ошибка: деление на 0.')
            print('Повторите ввод.')
            continue
        print('Результат = ', d3)
        if input('Прервать ввод? (q): ') == 'q':
            break

