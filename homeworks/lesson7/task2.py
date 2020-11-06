"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    """ Абстрактный класс одежды """

    def __init__(self, name):
        """ Инициализация инстанса класса

        :param name: название одежды
        """
        self.__name = name

    @property
    def name(self) -> str:
        """ Свойство возвращает название одежды

        :return: название одежды
        """
        return self.__name

    @abstractmethod
    def calc_cloth_size(self):
        """ Абстрактный метод, который должен быть переопредлен в потомках.
        Расчет размер ткани, необходимой для пошива одежды.
        """
        pass


class Coat(Clothes):
    """ Класс пальто """

    def __init__(self, size: float):
        """ Инициализация инстанса класса

        :param size: размер пальто
        """
        super().__init__('Пальто')
        self.__size = size

    @property
    def size(self) -> float:
        """ Свойство возвращает размер пальто

        :return: размер пальто
        """
        return self.__size

    def calc_cloth_size(self) -> float:
        """ Метод производит расчет размера ткани

        :return: размер ткани
        """
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f'<Coat(size={self.__size})>'


class Suit(Clothes):
    """ Класс костюма """
    def __init__(self, height: float):
        """ Инициализация инстанса класса

        :param height: рост
        """
        super().__init__('Костюм')
        self.__height = height

    @property
    def height(self) -> float:
        """ Свойство возвращает рост костюма

        :return: рост
        """
        return self.__height

    def calc_cloth_size(self) -> float:
        """ Метод производит расчет размера ткани

        :return: размер ткани
        """
        return 2 * self.__height + 0.3

    def __str__(self):
        return f'<Suit(height={self.__height})>'


if __name__ == '__main__':
    clothes = [Coat(1234), Suit(176), Suit(180), Coat(1567)]
    for cloth in clothes:
        print(f'Размер ткани для {cloth}: ', cloth.calc_cloth_size())
