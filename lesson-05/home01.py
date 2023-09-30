# 1. Напишите функцию is_year_leap, которая принимает число (год)
# и возвращает True если год високосный, False если нет.

def is_year_leap(inp):
    if inp % 100 == 0 and inp % 400 != 0 or inp % 4 != 0:
        return False
    elif inp % 400 == 0 or inp % 4 == 0:
        return True


assert (is_year_leap(2000)) is True
assert (is_year_leap(1900)) is False
assert (is_year_leap(1968)) is True
assert (is_year_leap(1967)) is False