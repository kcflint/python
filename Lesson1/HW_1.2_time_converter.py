time = int(input('Введите время в сеундах: '))
print(f'Вы ввели {time} секунд(у/ы)')

hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

if hours < 10:
    hours = str(f'0{hours}')
if minutes < 10:
    minutes = str(f'0{minutes}')

print(f'Ваше время в формате ЧЧ:ММ:СС {hours}:{minutes}:{seconds}')
