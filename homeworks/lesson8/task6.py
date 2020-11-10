"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class OfficeEquipment:

    def __init__(self, name, brand, model, price):
        self.__name = name
        self.__brand = brand
        self.__model = model
        self.__price = price


class Printer(OfficeEquipment):

    def __init__(self, brand, model, price, color):
        super().__init__('Принтер', brand, model, price)
        self.__color = color


class Scanner(OfficeEquipment):

    def __init__(self, brand, model, price, type):
        super().__init__('Сканер', brand, model, price)
        self.__type = type


class Xerox(OfficeEquipment):

    def __init__(self, brand, model, price, tank_size):
        super().__init__('Ксерокс', brand, model, price)
        self.__tank_size = tank_size


class StockOfficeEquipment:

    def __init__(self, name):
        self.__name = name
        self.__items = {}

    def add(self, department: str, equipment, amount: int = 1):
        if not isinstance(equipment, OfficeEquipment):
            raise ValueError('Object must be a OfficeEquipment')

        self.__items.setdefault(department, []).extend([equipment] * amount)

    def __str__(self):
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
