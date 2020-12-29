# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

class OwnError(Exception):
    pass


def zero_div():
    number1 = int(input("Введите делимое "))
    number2 = int(input("Введите делитель "))
    try:
        answer = number1 / number2
    except ZeroDivisionError:
        raise OwnError
    return answer

try:
    print(f"Результат деления {zero_div()}")
except OwnError:
    print("Деление на ноль невозможно")
