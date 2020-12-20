# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника, на позиции '{self.position}': {self.name} {self.surname}")

    def get_total_income(self):
        print("Полный доход сотрудника", self._income["wage"] + self._income["bonus"])


worker1 = Position('Вася', 'Пупкин', 'юморист', 1500, 200)
worker1.get_full_name()
worker1.get_total_income()

worker2 = Position('Виктор', 'Железогло', 'контролер', 1700, 400)
worker2.get_full_name()
worker2.get_total_income()
