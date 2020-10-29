"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import os
import re
import sys
import json

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(DIR, '..'))

from helpers import my_avg


COMPANIES = os.path.join(DIR, 'companies.txt')


def main():
    pattern = re.compile(
        r'(?P<name>[\w ]+)\s+'
        r'(?P<form>[А-Я]+)\s+'
        r'(?P<proceeds>[\d]+)\s+'
        r'(?P<costs>[\d]+)',
    )

    companies_profit = {}
    result, profits = [], []
    with open(COMPANIES, 'r') as f:
        for line in f:
            line_parse = pattern.match(line)
            if line_parse:
                profit = int(line_parse['proceeds']) - int(line_parse['costs'])
                companies_profit[line_parse['name']] = profit
                if profit > 0:
                    profits.append(profit)

    result.append(companies_profit)
    result.append({
        'average_profit': my_avg(profits),
    })

    with open(os.path.join(DIR, 'result.json'), 'w') as f:
        json.dump(result, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
