"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
from helpers import my_map, my_sum


global_sum = 0
while True:
    digits_str = input('Введите набор чисел разделенный пробелами: ')
    digits_list = digits_str.split()

    try:
        digits_sum = my_sum(my_map(int, digits_list))
    except ValueError:
        print('В последовательности есть нечисловые символы. Повторите ввод.')
        continue

    global_sum += digits_sum

    print('Сумма введенных чисел: ', digits_sum)

    if input('Прервать ввод? (y/n): ').lower() == 'y':
        break

print('Результат: ', global_sum)
