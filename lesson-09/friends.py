# Импортируйте класс Person из первого задания
# from person import Person
# 3. Создайте переменную my_friends - список из объектов класса
# Person. Добавьте в него некоторое количество вымышленных
# друзей с разными именами, возрастом и полом.
# 4. Выведите информацию о каждом друге на экран.
# 5. Найдите среди друзей самого старшего, выведите
# информацию о нём на экран.
# 6. Выведите на экран информацию о всех друзьях мужского пола
# (можно использовать функцию filter, либо генератор списков).
# 7. Заверните код из пунктов 5 и 6 в функции get_oldest_person и
# filter_male_person соответственно.


from person import Person

my_friends = []
my_friends.append(Person('James Gunn', 57, 'M'))
my_friends.append(Person('Roisin Murphy', 50, 'F'))
my_friends.append(Person('Emma Stone', 34, 'F'))
my_friends.append(Person('Peter Capaldi', 65, 'M'))
my_friends.append(Person('Margot Robbie', 33, 'F'))
my_friends.append(Person('John Cena', 46, 'M'))


def get_oldest_person(self):
    oldest_person = my_friends[0]
    for p in my_friends:
        if p.age > oldest_person.age:
            oldest_person = p
    print(f"The oldest person is {oldest_person.name} ({oldest_person.age} years old).")


def filter_male_person(self):
    male_friends = [person for person in my_friends if person.gender == 'M']
    print(f' There are male friends of mine:')
    for person in male_friends:
        print(f'{person.name}, {person.age} years old')


get_oldest_person(my_friends)

filter_male_person(my_friends)


# male_friends = list(filter(lambda person: person.gender == 'M', my_friends))
# for person in male_friends:
#     print(f'{person.name}, {person.age} years old')