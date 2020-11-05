"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '..'))

from helpers import my_sum, my_map


FILE_NAME = os.path.join(DIR, 'task5_file.txt')


def main():
    digits = [1, 3, 4, 4, 77, 3, 2, 9, 7, 4, 7]
    digits_row = ' '.join(my_map(str, digits))

    with open(FILE_NAME, 'w') as f:
        f.write(digits_row)

    with open(FILE_NAME, 'r') as f:
        digits_str = f.read()

    digits_sum = my_sum((int(digit) for digit in digits_str.split()))

    print('Результат: ', digits_sum)


if __name__ == '__main__':
    main()
