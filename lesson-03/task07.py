# 7. * Пользователь вводит число, выведите True если оно простое, иначе False.

num = int(input('Enter a number . If it is prime, the program will output "True", if not - "False" '))
i = 2
if num <= 1:
    print('False. Prime numbers start with 2. Google for details ')
elif num > 1:
    while num % i != 0:
     i += 1
    print(num == i)