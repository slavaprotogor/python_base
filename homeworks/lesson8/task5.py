"""
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
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

    def add(self, department: str, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise ValueError('Object must be a OfficeEquipment')

        self.__items.setdefault(department, []).append(equipment)

    def __str__(self):
        return str(self.__items)


if __name__ == '__main__':
    printer1 = Printer('Canon', 'MP-12900', 12000, 'Черно-белый')
    printer2 = Printer('Samsung', 'SM-900', 15000, 'Цветной')
    scanner = Scanner('Sony', 'M-9300', 35000, 'Барабанный')
    xerox = Xerox('Ксерокс', 'VD-2250', 20000, 3000)

    stock = StockOfficeEquipment('Склад Эльдорадо')
    stock.add('Бухгалтерия', printer1)
    stock.add('Отдел кадров', printer2)
    stock.add('Бухгалтерия', scanner)
    stock.add('Отдел кадров', xerox)

    print(stock)
