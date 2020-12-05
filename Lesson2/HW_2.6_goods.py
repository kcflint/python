goods = []
name_list = []
price_list = []
number_list = []
unit_list = []
number = int(input('Введите число наименований товаров: '))

for i in range(number):
    print(f'Товар номер {i + 1}')
    user_good = input('Введите название товара: ')
    user_price = input('Введите стоимость товара: ')
    user_number = input('Введите количество товара: ')
    user_unit = input('Введите единицы измерения товара: ')
    user_dict = {'название товара': user_good, 'цена товара': user_price, 'количсетво штук': user_number, 'единицы измерения': user_unit}
    user_tuple = (i + 1, user_dict)
    goods.append(user_tuple)

    name_list.append(goods[i][1]['название товара'])
    price_list.append(goods[i][1]['цена товара'])
    number_list.append(goods[i][1]['количсетво штук'])
    unit_list.append(goods[i][1]['единицы измерения'])

print('Список товаров:')
for i in range(number):
    print(goods[i])

print('Аналитика товаров')
print('Наименования товаров:', name_list)
print('Цены товаров:', price_list)
print('Число товаров:', number_list)
print('Единицы измерения:', unit_list)
