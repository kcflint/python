distance = int(input('Сколько километров спортсмен пробежал в первый день? '))
goal = int(input('Какое количество километров спортсмен должен пробежать в сумме? '))

total = distance
days = 1
print(f'{days}-й день: {distance} км')
while total < goal:
    distance = 1.1 * distance
    total = total + distance
    days += 1
    print(f'{days}-й день: {distance:.1f} км')
print(f'Спортсмен пробежал {total:.1f} км')
print(f'На {days}-й день спортсмен достиг результата не менее {goal} километров в сумме')
