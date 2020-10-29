"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import os


DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(DIR, 'task1_file.txt')


def main():
    with open(FILE_NAME, 'w') as f:
        while True:
            line = input('Введите строку: ')
            if not line:
                break
            f.write(line + '\n')
        print('Ввод окончен.')


if __name__ == '__main__':
    main()
