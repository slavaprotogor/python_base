"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""
import re
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '..'))

from helpers import parse_to_int


TIMETABLE = os.path.join(DIR, 'timetable.txt')


def main():
    pattern = re.compile(
        r'(?P<name>[\w ]+):\s+'
        r'(?P<lects>([\d]+\(л\)|—))\s+'
        r'(?P<pracs>([\d]+\(пр\)|—))\s+'
        r'(?P<labs>([\d]+\(лаб\)|—))',
    )

    lessons = {}
    with open(TIMETABLE, 'r') as f:
        for line in f:
            line_parse = pattern.match(line)
            if line_parse:
                lessons[line_parse['name']] = parse_to_int(line_parse['lects']) + \
                    parse_to_int(line_parse['pracs']) + parse_to_int(line_parse['labs'])

    print('Результат: ', lessons)


if __name__ == '__main__':
    main()
