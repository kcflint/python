# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + "+" + str(self.b) + "i"

    def __add__(self, other):
        return str(self.a + other.a) + "+" + str(self.b + other.b) + "i"

    def __mul__(self, other):
        return str(self.a * other.a - self.b * other.b) + "+" + str(self.a * other.b + self.b * other.a) + "i"

sample1 = Complex(1, 3)
print(sample1)
sample2 = Complex(-2, -1)
print(sample2)
print("Сложение комплексных чисел", sample1 + sample2)
print("Умножение комплексных чисел", sample1 * sample2)
