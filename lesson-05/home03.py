# 3. Напишите функцию generate_squares, которая принимает
# произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.
# То есть generate_squares(1, 2, 3) -> [1, 4, 9]

def generate_squares(*args):
    square = [i**2 for i in args]
    return square


assert generate_squares(3, 6, 7, 2) == [9, 36, 49, 4]