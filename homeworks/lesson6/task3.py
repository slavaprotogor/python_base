"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        """ Инициализация инстанса класса

        :param name: имя
        :param surname: фамилия
        :param position: должность
        :param wage: ставка
        :param bonus: премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }


class Position(Worker):

    def get_full_name(self):
        """ Вывод полного имени

        :return: полное имя
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """ Вывод общего дохода

        :return: общий доход
        """
        return self._income['wage'] + self._income['bonus']


person1 = Position('Ivan', 'Ivanov', 'boss', 100000, 50000)

assert person1.get_full_name() == 'Ivan Ivanov', 'Ошибка'

assert person1.get_total_income() == 150000, 'Ошибка'


person2 = Position('Petr', 'Petrov', 'programmist', 300000, 50000)

assert person2.get_full_name() == 'Petr Petrov', 'Ошибка'

assert person2.get_total_income() == 350000, 'Ошибка'
