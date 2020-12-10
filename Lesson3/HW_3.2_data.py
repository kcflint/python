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


def data(name, surname, year, city, email, phone):
    print('Первый способ')
    print(f'имя - {name}; фамилия - {surname}; год рождения - {year}; город проживания - {city};'
          f'email - {email}; номер телефона - {phone}')


data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone)

# Второй способ


def data(**kwargs):
    return kwargs


print('Второй способ')
print(data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone))
