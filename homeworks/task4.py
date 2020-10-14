"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
# version 1
number_list = list(input('Введите число: '))

max_value = 0
while number_list:
    value = int(number_list.pop())
    if value > max_value:
        max_value = value

print('Максимальное число =', max_value)

# version 2
number_str = input('Введите число: ')
number_len = len(number_str)

max_value = 0
while number_len:
    number_len -= 1
    value = int(number_str[number_len])
    if value > max_value:
        max_value = value

print('Максимальное число =', max_value)

