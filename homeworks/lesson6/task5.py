"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self._title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return 'Пишет ручка'


class Pencil(Stationery):

    def draw(self):
        return 'Чертит карандаш'


class Handle(Stationery):

    def draw(self):
        return 'Рисует маркер'


pen = Pen('Ручка')
assert pen.draw() == 'Пишет ручка', 'Ошибка'

pencil = Pencil('Карандаш')
assert pencil.draw() == 'Чертит карандаш', 'Ошибка'

handle = Handle('Маркер')
assert handle.draw() == 'Рисует маркер', 'Ошибка'
