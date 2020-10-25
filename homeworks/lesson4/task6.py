"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее
"""
from helpers import input_int, my_count, my_range, my_cycle


duration = input_int('Длительность вывода элементов (сек.): ')

# вывод элементов
for item in my_count(0, 1, duration):
    print(item)

# зацикленный вывод элементов
for item in my_cycle('ABCD', duration):
    print(item)

# ограниченный вывод последовательности
for item in my_range(50):
    print(item)
