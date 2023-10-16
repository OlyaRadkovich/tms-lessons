# Создайте класс Student, с полями full_name, average_mark (средняя оценка).
# Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию данного студента по следующему алгоритму:
# Если средняя оценка < 6 - вернуть 60 (рублей)
# Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
# Если средняя оценка >= 8 - вернуть 100 (рублей)
# Добавить в класс метод is_excellent, который возвращает bool:
# True, если средняя оценка >= 9
# False, иначе

class Student:
    def __init__(self, full_name, average_mark):
        self.name = full_name
        self.average = int(average_mark)

    def get_scholarship(self):
        scholarship = 0
        if self.average < 6:
            scholarship = 60
        elif 6 <= self.average < 8:
            scholarship = 80
        elif self.average >= 8:
            scholarship = 100
        return int(scholarship)
        # return f'Начислена стипендия {int(scholarship)} рублей'

    def is_excellent(self):
        return self.average >= 9





