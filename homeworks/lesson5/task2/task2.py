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
    for line_index, words_count in file_stat(FILE_NAME):
        print(f'Номер строки: {line_index}, кол-во слов: {words_count};')


if __name__ == '__main__':
    main()
