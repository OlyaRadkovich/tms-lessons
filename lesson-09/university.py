# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count


from student import Student


students_list = []
students_list.append(Student('Максим Пархимович', 8))
students_list.append(Student('Мария Юран', 7))
students_list.append(Student('Артем Тесов', 5))
students_list.append(Student('Юлия Воробьева', 10))
students_list.append(Student('Татьяна Ермоленко', 9))

# проверка
# for student in students_list:
#     print(student.name,':')
#     print(f'Начислена стипендия {student.get_scholarship()} рублей')
#     print(student.is_excellent())


def calc_sum_scholarship(students_list):
    scholarship_sum = 0
    for student in students_list:
        scholarship_sum += student.get_scholarship()
    print(f'Суммарная стипендия: {scholarship_sum} рублей')


def get_excellent_student_count(students_list):
    excellent_students = sum(1 for student in students_list if student.is_excellent())
    print(f'Отличников в группе: {excellent_students}')

calc_sum_scholarship(students_list)
get_excellent_student_count(students_list)



    # excellent_students = 0
    # for student in students_list:
    #      if student.is_excellent() == True:
    #         excellent_students += 1
    # print(f'Отличников в группе: {excellent_students}')
