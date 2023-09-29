# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу. Если он ответил “no” - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать,
# пока ответ не будет корректным.

for i in range(0,101):
    print(i)
    should_break = input('Should we break?').lower()
    while should_break == 'no':
        i += 1
        print(i)
        should_break = input('Should we break? ').lower()
        while should_break != 'yes' and should_break != 'no':
            should_break = input("Don't understand you ").lower()
    else:
         break