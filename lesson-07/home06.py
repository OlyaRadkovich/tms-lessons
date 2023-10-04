# Решите прошлую задачу так, чтобы ваш декоратор работал для любой функции, с любым количеством параметров.
# А также? чтобы работал с именованными параметрами.
# Подсказка: используйте *args и **kwargs.


def my_decorator(func):
    def my_wrapper(*args, **kwargs):
        print(f'Функция получила на вход: {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'Результат функции: {result}')
        return result
    return my_wrapper


@my_decorator
def my_plus(a, b, c, d):
    return a + b + c + d

y = my_plus(41, b=2, d=3, c=7)

print(f'y = {y}')
