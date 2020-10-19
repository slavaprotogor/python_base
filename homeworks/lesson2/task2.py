"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

elements = []
while True:
    element = input('Введите элемент (q - выход): ')
    if element == 'q':
        break
    elements.append(element)

elements_odd = elements[::2]
elements_odd_len = len(elements_odd)

elements_even = elements[1::2]
elements_even_len = len(elements_even)

elements_new = []
for index in range(elements_odd_len):
    if index < elements_even_len:
        elements_new.append(elements_even[index])
    elements_new.append(elements_odd[index])

print('Результат: ', elements_new)
