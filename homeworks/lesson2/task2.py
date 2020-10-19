"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
# version 1
elements = []
while True:
    element = input('Введите элемент (q - выход): ')
    if element == 'q':
        break
    elements.append(element)

elements_len = len(elements)
index = 1
while index < elements_len:
    element = elements[index]
    elements[index] = elements[index - 1]
    elements[index - 1] = element
    index += 2

print('Результат: ', elements)

# version 2
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
