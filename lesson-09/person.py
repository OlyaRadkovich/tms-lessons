# Создайте класс Person. У класса должно быть три поля: full_name, age, gender, которые должны заполняться в
# конструкторе. Будем считать что поле gender имеет тип str и может быть либо 'M' (male), либо 'F' (female).
# Добавьте в класс метод print_person_info, который печатает на экран строку:
# "Person: {full_name} ({gender}), {age} years old"
# Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
# * Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год).
# Текущий год можно взять с помощью модуля datetime (пример).

class Person:

    def __init__(self, full_name, age, gender):
        self.name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
       print(f'Person: {self.name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        import datetime
        current_year = datetime.datetime.now().year
        return f'Was born in {current_year - int(self.age)}'


# # создание объекта
# p = Person ('Peter Capaldi', '65', 'M')
#
#         # обращение к полям класса
# print(p.name)
# print(p.age)
# print(p.gender)
#
#         # вызов метода класса и вывод результата на экран
# p.print_person_info()
#
#         # вызов метода класса + вывод изменившегося поля
# print(p.get_birth_year())

