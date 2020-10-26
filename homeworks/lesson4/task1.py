"""
 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys


def formula_salary(hs: float, hp: float, b: float) -> float:
    """
    Формула расчета заработной платы.
    salary = hr * hp + b

    :param hs: отработаных часов
    :param hp: ставка плата за час работы
    :param b: перемия
    :return: зарплата
    """
    return hs * hp + b


try:
    hours, hour_pay, bonus = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    print('Зарплата = ', formula_salary(hours, hour_pay, bonus))
except ValueError:
    print('Все параметры должны быть числовыми')
except IndexError:
    print('Должно быть задано минимум 3 параметра')
