# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделитель
# и возвращает строку, в которой все слова из списка соединены через символ разделитель.
# Пример ввода пользователя:
# hello this is my string
# @
# Вывод программы: hello@this@is@my@string
# Используйте функцию reduce

from functools import reduce
custom_sentence = input('Enter several words:  ').split()
custom_symbol = input('Enter a symbol:  ')[0]


def my_join(str1, str2):
    return str1 + custom_symbol + str2


new_sentence = reduce(my_join, custom_sentence)
print(new_sentence)