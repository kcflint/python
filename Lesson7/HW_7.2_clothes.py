# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property .

class Clothes:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"{self.title}"


class Coat(Clothes):
    def __init__(self, title, size):
        self.__type = "Clothes"
        super().__init__(title)
        self.size = size

    @property
    def fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, title, size):
        self.__type = "Clothes"
        super().__init__(title)
        self.size = size

    @property
    def fabric(self):
        return 2 * self.size + 0.3

a = Coat("Плащ", 3)
print(f"Расход ткани {a} {a.fabric:.2f}")
b = Suit("Костюм", 23)
print(f"Расход ткани {b} {b.fabric:.2f}")
print(f"Общий расход ткани {a.fabric+ b.fabric:.2f}")
