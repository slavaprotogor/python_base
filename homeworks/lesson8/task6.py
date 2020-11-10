"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipment:
    """ Базовый класс оргтехники """

    def __init__(self, name: str, brand: str, model: str, price: int):
        """ Инициализация

        :param name: название
        :param brand: бренд
        :param model: модель
        :param price: цена
        """
        self.__name = name
        self.__brand = brand
        self.__model = model
        self.__price = price


class Printer(OfficeEquipment):
    """ Класс принтера """

    def __init__(self, brand, model, price, color):
        """ Инициализация

        :param brand: бренд
        :param model: модель
        :param price: цена
        :param color: цыет печати
        """
        super().__init__('Принтер', brand, model, price)
        self.__color = color


class Scanner(OfficeEquipment):
    """ Класс сканера """

    def __init__(self, brand, model, price, type):
        """ Инициализация

        :param brand: бренд
        :param model: модель
        :param price: цена
        :param type: тип сканера
        """
        super().__init__('Сканер', brand, model, price)
        self.__type = type


class Xerox(OfficeEquipment):
    """ Класс ксерокса """

    def __init__(self, brand, model, price, tank_size):
        """ Инициализация

        :param brand: бренд
        :param model: модель
        :param price: цена
        :param tank_size: рахмер бака
        """
        super().__init__('Ксерокс', brand, model, price)
        self.__tank_size = tank_size


class StockOfficeEquipment:
    """ Класс склада """

    def __init__(self, name):
        """ Инициализация

        :param name: название
        """
        self.__name = name
        self.__items = {}

    def add(self, department: str, equipment, amount: int = 1):
        """ Добавление элемена в склад

        :param department: отдел
        :param equipment: оргтехника
        :param amount: количество
        :return: None
        """
        if not isinstance(equipment, OfficeEquipment):
            raise ValueError('Object must be a OfficeEquipment')

        self.__items.setdefault(department, []).extend([equipment] * amount)

    def __str__(self):
        """ Строковое представление

        :return: строковое представление
        """
        return str(self.__items)


if __name__ == '__main__':
    printer1 = Printer('Canon', 'MP-12900', 12000, 'Черно-белый')
    printer2 = Printer('Samsung', 'SM-900', 15000, 'Цветной')
    scanner = Scanner('Sony', 'M-9300', 35000, 'Барабанный')
    xerox = Xerox('Ксерокс', 'VD-2250', 20000, 3000)

    stock = StockOfficeEquipment('Склад Эльдорадо')
    stock.add('Бухгалтерия', printer1, 4)
    stock.add('Отдел кадров', printer2, 5)
    stock.add('Бухгалтерия', scanner, 2)
    stock.add('Отдел кадров', xerox, 5)

    print(stock)
