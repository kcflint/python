# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, unit_mass, height):
        mass = self._length * self._width * unit_mass * height
        print(f"Масса асфальта, необходимая для покрытия всего дорожного полотна, длинной {self._length} м, "
              f"шириной {self._width} м, толщиной {height} см, равна {mass} кг")


road1 = Road(5000, 20)
road1.calculation(2, 5)
