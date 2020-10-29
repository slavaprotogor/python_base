"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '..'))

from helpers import file_stat


FILE_NAME = os.path.join(DIR, 'task2_file.txt')


def main():
    line_count, word_count = file_stat(FILE_NAME)

    print(f'Кол-во линий в файле: {line_count};\n'
          f'Кол-во слов в файле: {word_count};')


if __name__ == '__main__':
    main()
