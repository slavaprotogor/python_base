"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

element_types = {
    str: 'строка',
    int: 'целое число',
    float: 'число с плавающей точкой',
    list: 'список',
    dict: 'словарь',
    tuple: 'кортеж',
    set: 'множество',
    frozenset: 'неизменяемое множество',
    type(None): 'ничто',
}

elements = [
    'element',
    33,
    222.99,
    ['1', 3],
    {'a': 1, 'b': 'example'},
    ('r', 'd'),
    {1, 2, 3, 1},
    frozenset(('2', 2, ('a', 'b', 'c'))),
    None,
]

for element in elements:
    element_type = element_types.get(type(element))
    if element_type is not None:
        print(f'Элемент {element} - {element_type}')
    else:
        print(f'Элемент {element} имеет незвестный тип')

