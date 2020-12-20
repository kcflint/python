# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title)
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(self.title)
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print(self.title)
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print(self.title)
        print("Запуск отрисовки уникальный")


sample1 = Stationery("Образец 1")
sample1.draw()
sample2 = Pen("Образец 2")
sample2.draw()
sample3 = Pencil("Образец 3")
sample3.draw()
sample4 = Handle("Образец 4")
sample4.draw()
