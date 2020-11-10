"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
import copy


class ItemDigitError(ValueError):
    pass


class MyList:

    def __init__(self, *args):
        if args:
            if not all((self._is_digit(item) for item in args)):
                raise ItemDigitError('Some item is not a digit')

        self.__items = list(copy.deepcopy(args)) if args else []

    def _is_digit(self, value):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    def append(self, item):
        if not self._is_digit(item):
            raise ItemDigitError('Item is not a digit')

        self.__items.append(item)

    def __str__(self):
        return str(self.__items)


if __name__ == '__main__':
    items = MyList('3', '3', '4')
    while True:
        digit = input('Введите число: ')
        try:
            items.append(digit)
        except ItemDigitError:
            print('Введенное значение не является числом')
            print('Повторите ввод')
            continue

        if input('Завершить ввод? (q): ') == 'q':
            break

    print('Введенные данные', items)
