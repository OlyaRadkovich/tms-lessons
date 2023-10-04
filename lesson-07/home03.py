#  Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
#  Вам по прежнему нужно удалить все гласные. При этом результат нужно вывести,
#  сохранив изначальный регистр.

custom_list = input('Enter random English letters separated by spaces: ').split()
def remove_vowels(letter):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    if letter in vowels:
        return False
    else:
        return True


new_list = list(filter(remove_vowels, custom_list))
print(new_list)