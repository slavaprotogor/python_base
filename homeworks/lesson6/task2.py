"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
Проверить работу метода.
"""


class Road:

    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def calc_weight(self, height: int, weight_rect: int):
        return self.__length * self.__width * height * weight_rect


road = Road(20, 5000)
assert road.calc_weight(0.05, 25) == 125000, "Calculation error"
