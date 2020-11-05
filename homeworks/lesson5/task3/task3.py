"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import re
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '..'))

from helpers import my_avg


FILE_NAME = os.path.join(DIR, 'salaries.txt')


def main():
    pattern = re.compile(
        r'(?P<surname>[\w ]+)\s+'
        r'(?P<salary>[\d]+)'
    )

    workers = []
    with open(FILE_NAME, 'r') as f:
        for line in f:
            line_parse = pattern.match(line)
            if line_parse:
                workers.append((line_parse['surname'], int(line_parse['salary'])))

    workers_poor = [worker for worker in workers if worker[1] < 20000]
    print('Работники с окладом меньше 20 тыс.: ', workers_poor)

    salary_avg = my_avg([worker[1] for worker in workers])
    print('Средняя зарплата: ', salary_avg)


if __name__ == '__main__':
    main()
