# Пользователь вводит произвольное количество латинских букв через пробел. Буквы могут быть как в верхнем,
# так и в нижнем регистре (на результат работы это влиять не должно).
# Напишите функцию map_to_tuples, которая принимает список из этих букв и возвращает список из кортежей.
# В каждом кортеже первой должна идти буква в верхнем регистре, а второй эта же буква в нижнем.
# Выведите результат работы функции на экран.


custom_list = input('Enter random English letters separated by spaces: ').split()


def map_to_tuples(letter):
    return letter.upper(), letter.lower()


new_list = list(map(map_to_tuples, custom_list))
print(new_list)
