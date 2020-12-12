# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = int(input('Введите месяц в виде целого числа от 1 до 12: '))


# Через списки
list_month = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
list_season = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer',
               'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
print('Через списки:')
print(month, list_month[month-1], list_season[month-1])

# Через словари 1
dict_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dict_season = {1: 'Winter', 2: 'Winter', 12: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
               6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}
print('Через словари:')
print(month, dict_month[month], dict_season[month])

# Через словари 2
dict_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dict_season = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
print('Через словари:')
if month in dict_season['Winter']:
    print(month, dict_month[month], 'Winter')
elif month in dict_season['Spring']:
    print(month, dict_month[month], 'Spring')
elif month in dict_season['Summer']:
    print(month, dict_month[month], 'Summer')
elif month in dict_season['Autumn']:
    print(month, dict_month[month], 'Autumn')
