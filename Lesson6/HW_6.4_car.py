# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name}", self.speed)


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name}", self.speed)
        if self.speed > 60:
            print("Скорость превышена!")


class SportCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name}", self.speed)
        if self.speed > 40:
            print("Скорость превышена!")


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


car1 = Car(40, "красная", "Ferrari", False)
car1.go()
car1.turn("налево")
car1.show_speed()
car1.stop()

car2 = TownCar(80, "зеленый", "Жигули", False)
car2.go()
car2.show_speed()
car2.turn("направо")
car2.stop()

car3 = SportCar(42, "синий", "Bugatti", False)
car3.go()
car3.show_speed()
car3.turn("направо")
car3.stop()

car4 = WorkCar(65, "белый", "Pigeout", False)
car4.go()
car4.show_speed()
car4.turn("направо")
car4.stop()

car5 = PoliceCar(70, "черная", "Toyota", True)
car5.go()
car5.show_speed()
car5.turn("налево")
car5.stop()
