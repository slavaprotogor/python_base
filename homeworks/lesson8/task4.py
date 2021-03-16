"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
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
        self.__items = []

    def add(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise ValueError('Object must be a OfficeEquipment')

        self.__items.append(equipment)

    def __str__(self):
        return str(self.__items)


if __name__ == '__main__':
    printer1 = Printer('Canon', 'MP-12900', 12000, 'Черно-белый')
    printer2 = Printer('Samsung', 'SM-900', 15000, 'Цветной')
    scanner = Scanner('Sony', 'M-9300', 35000, 'Барабанный')
    xerox = Xerox('Ксерокс', 'VD-2250', 20000, 3000)

    stock = StockOfficeEquipment('Склад Эльдорадо')
    stock.add(printer1)
    stock.add(printer2)
    stock.add(scanner)
    stock.add(xerox)

    print(stock)
