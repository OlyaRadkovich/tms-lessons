# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
# Используйте функцию filter.
# Список всех гласных английского языка: a, e, i, o, u

custom_list = input('Enter random English letters in lower case separated by spaces: ').split()

def remove_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter in vowels:
        return False
    else:
        return True


new_list = list(filter(remove_vowels, custom_list))
print(new_list)