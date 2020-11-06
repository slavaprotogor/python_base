"""
Создать (не программно) текстовый файл со следующим содержимым: One — 1, Two — 2, Three — 3, Four — 4.
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
import os


digit_mapper = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

DIR = os.path.dirname(os.path.abspath(__file__))
FILE_READ = os.path.join(DIR, 'task4_read.txt')
FILE_WRITE = os.path.join(DIR, 'task4_write.txt')


def main():
    with open(FILE_READ, 'r') as f_read:
        with open(FILE_WRITE, 'w') as f_write:
            for line in f_read:
                number, hyphen, digit = line.split()
                f_write.write(f'{digit_mapper[number]} {hyphen} {digit}\n')

    print('Операция окончена.')


if __name__ == '__main__':
    main()
