# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

user_word = input('Введите слова латинскими буквами через пробел ')
# Первый способ


def int_func1(arg1):
    line = ''
    for i in range(len(user_word1)):
        word = list(arg1[i])
        letter = word[0].upper()
        word[0] = letter
        line += ''.join(word) + " "
    print('Первый способ:', line)


user_word1 = user_word.split()
int_func1(user_word1)

# Второй способ


def int_func(arg1):
    return arg1.title()


print('Второй способ:', int_func(user_word))

# Третий способ


def int_func3(arg3):
    for i in range(len(user_word3)):
        arg3[i] = arg3[i].capitalize()
    return arg3


user_word3 = user_word.split()
print("Третий способ:", ' '.join(int_func3(user_word3)))
