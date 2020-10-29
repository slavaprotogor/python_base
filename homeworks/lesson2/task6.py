"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""


def input_int(message):
    digit = ''
    while not digit.isdigit():
        digit = input(message)
    return int(digit)


product_columns = [
    {'name': 'name', 'type': 'str', 'message': 'Введите название товара: '},
    {'name': 'price', 'type': 'int', 'message': 'Введите цену товара: '},
    {'name': 'quantity', 'type': 'int', 'message': 'Введите количество товара: '},
    {'name': 'unit', 'type': 'str', 'message': 'Введите единицу измерения товара: '},
]

type_inputs = {
    'str': input,
    'int': input_int,
}

product_number = input_int('Введите количество товара (число): ')

products = []
for index in range(1, product_number + 1):
    print(f'Продукт {index}: ')
    product_item = {}
    for column in product_columns:
        product_item[column['name']] = type_inputs[column['type']](column['message'])
    products.append((index, product_item))

products_analitic = {}
for index, product in products:
    for name, value in product.items():
        if name == 'unit':
            products_analitic.setdefault(name, set()).add(value)
        else:
            products_analitic.setdefault(name, []).append(value)

print(products_analitic)
