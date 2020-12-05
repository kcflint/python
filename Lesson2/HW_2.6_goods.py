goods = []
name_list = []
price_list = []
number_list = []
number = int(input('Введите число наименований товаров: '))

for i in range(number):
    print(f'Товар номер {i+1}')
    user_good = input('Введите название товара: ')
    user_price = input('Введите стоимость товара: ')
    user_number = input('Введите количество товара: ')
    user_dict = {'название товара': user_good, 'цена товара': user_price, 'количсетво штук': user_number}
    user_tuple = (i+1, user_dict)
    goods.append(user_tuple)
    name_list.append(user_good)
    price_list.append(user_price)
    number_list.append(user_number)

good_dict = {'название товара': name_list, 'цена товара': price_list, 'количсетво штук': number_list}

print('Список товаров:')
for i in range(number):
    print(goods[i])

print('Аналитика товаров')
print('Наименования товаров:', good_dict['название товара'])
print('Цены товаров:', good_dict['цена товара'])
print('Число товаров:', good_dict['количсетво штук'])
