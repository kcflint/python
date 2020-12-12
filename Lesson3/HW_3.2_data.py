# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.


user_name = input('Введите свое имя:')
user_surname = input('Введите свою фамилию:')
user_year = input('Введите год своего рождения:')
user_city = input('Введите город проживания:')
user_email = input('Введите свой email:')
user_phone = input('Введите свой номер телефона:')

# Первый способ


def data1(name1, surname1, year1, city1, email1, phone1):
    print('Первый способ')
    print(f'имя - {name1}; фамилия - {surname1}; год рождения - {year1}; город проживания - {city1};'
          f'email - {email1}; номер телефона - {phone1}')


data1(name1=user_name, surname1=user_surname, year1=user_year, city1=user_city, email1=user_email, phone1=user_phone)

# Второй способ


def data2(**kwargs):
    print(kwargs)


print('Второй способ')
data2(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone)
