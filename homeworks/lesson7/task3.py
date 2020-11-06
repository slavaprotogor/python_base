"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
 нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    """ Класс клеткаи """
    __slots__ = ('__cores',)

    def __init__(self, cores: int):
        """ Инициализация инстанса класса

        :param cores: количество ячеек
        """
        if not isinstance(cores, int):
            raise TypeError('Cores must be a integer')

        if cores <= 0:
            raise ValueError('Cores must be a positive integer')

        self.__cores = cores

    @property
    def cores(self):
        """ Свойство возвращает количество ячеек

        :return: кол-во ячеек
        """
        return self.__cores

    def __add__(self, other):
        """ Сложение клеток и получение новой клетки

        :param other: клетка, объект типа Cell
        :return: новая клетка
        """
        if not isinstance(other, Cell):
            raise TypeError('The object must be a Cell')

        return Cell(self.__cores + other.cores)

    def __sub__(self, other):
        """ Вычетание клеток и получение новой клетки

        :param other: клетка, объект типа Cell
        :return: новая клетка
        """
        if not isinstance(other, Cell):
            raise TypeError('The object must be a Cell')
        if other.cores >= self.__cores:
            raise ValueError('Cell cores more then cores of first Cell')

        return Cell(self.__cores - other.cores)

    def __mul__(self, other):
        """ Умножение клеток и получение новой клетки

        :param other: клетка, объект типа Cell
        :return: новая клетка
        """
        if not isinstance(other, Cell):
            raise TypeError('The object must be a Cell')

        return Cell(self.__cores * other.cores)

    def __truediv__(self, other):
        """ Деление клеток и получение новой клетки

        :param other: клетка, объект типа Cell
        :return: новая клетка
        """
        if not isinstance(other, Cell):
            raise TypeError('The object must be a Cell')

        return Cell(round(self.__cores / other.cores))

    def make_order(self, chunk_size: int) -> str:
        """ Метод рисует строковое представление ячеек
        клетки разделенных на группы

        :param chunk_size: размер группы
        :return: строковое представление ячеек
        """
        chunks, tail = divmod(self.__cores, chunk_size)

        cores_graph = ['*' * chunk_size for _ in range(chunks)]
        if tail:
            cores_graph.append('*' * tail)
        return '/n'.join(cores_graph)


if __name__ == '__main__':
    cell1 = Cell(23)
    cell2 = Cell(5)

    print('Сумма:')
    cell3 = cell1 + cell2
    print(cell3.make_order(5))

    print('Вычитание:')
    cell3 = cell1 - cell2
    print(cell3.make_order(5))

    print('Умножение:')
    cell3 = cell1 * cell2
    print(cell3.make_order(5))

    print('Деление:')
    cell3 = cell1 / cell2
    print(cell3.make_order(5))
