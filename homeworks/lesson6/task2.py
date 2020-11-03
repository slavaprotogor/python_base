"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length: int, width: int):
        """ Инициализация инстанса класса

        :param length: длина
        :param width: ширина
        """
        self._length = length
        self._width = width

    def calc_weight(self, height: float, weight_rect: int):
        """ Считает массу асфальта

        :param height: толщина
        :param weight_rect: масса асфальта для покрытия одного кв метра дороги асфальтом
        :return:
        """
        return self._length * self._width * height * weight_rect


road = Road(20, 5000)
assert road.calc_weight(0.05, 25) == 125000, "Calculation error"
