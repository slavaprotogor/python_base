"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
"""
from helpers import input_int, my_range, my_reduce


# version 1
def fact(number: int) -> int:
    """
    Факториал числа

    :param number: число
    :return: факториал числа
    """
    index = 1
    result = 1
    while index <= number:
        result *= index
        yield result
        index += 1
    else:
        raise StopIteration


number_fact = input_int('Факториал числа: ')

for idx, item in enumerate(fact(number_fact), 1):
    print(f'Факториал {idx} = ', item)


# version 2
number = input_int('Факториал числа: ')

print(f'Факториал числа {number}: ', my_reduce(my_range(number, 1), lambda x, y: x * y, 1))
