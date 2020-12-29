# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class Warehouse:
    OfficeEquipment_dict = {}


class OfficeEquipment:
    def __init__(self, company, model):
        self.company = company
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, company, model, sort):
        super().__init__(company, model)
        self.sort = sort

    def __str__(self):
        return f"{self.company}, {self.model}, {sort}"

    printer_dict = {}


class Scanner(OfficeEquipment):
    def __init__(self, company, model, kind):
        super().__init__(company, model)
        self.kind = kind

    def __str__(self):
        return f"{self.company}, {self.model}, {kind}"

    scanner_dict = {}


class Copier(OfficeEquipment):
    def __init__(self, company, model, color):
        super().__init__(company, model)
        self.color = color

    def __str__(self):
        return f"{self.company}, {self.model}, {color}"

    copier_dict = {}


a = Warehouse
name = ["Принтер", "Сканер", "Ксерокс"]
for i in range(len(name)):
    equipment_number = input(f"{name[i]}, количество штук, отправляемых на склад: ")
    while not equipment_number.isdigit():
        try:
            type(int(equipment_number)) == int
        except ValueError:
            print("Введите число")
            equipment_number = input(f"{name[i]}, количество штук, отправляемых на склад: ")
    for n in range(int(equipment_number)):
        print(f"{name[i]} номер {n+1}")
        company = input("Фирма-производитель: ")
        model = input("Модель: ")
        if i == 0:
            sort = input("Вид (матричный, струйный, лазерный): ")
            Printer.printer_dict.update({n+1: [company, model, sort]})
        if i == 1:
            kind = input("Вид (ручной, стационарный): ")
            Scanner.scanner_dict.update({n+1: [company, model, kind]})
        if i == 2:
            color = input("Вид (чернобелый, цветной): ")
            Copier.copier_dict.update({n+1: [company, model, color]})
    a.OfficeEquipment_dict.update({name[i]: equipment_number})

print("Список принтеров", Printer.printer_dict)
print("Список сканеров", Scanner.scanner_dict)
print("Список ксероксов", Copier.copier_dict)
print("Список оргтехники на складе", a.OfficeEquipment_dict)
sample2 = Scanner("Samsung", "C2", "Ручной")
sample3 = Copier("XeRox", "3b1", "Цветной")
