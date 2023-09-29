# Программа загадывает случайное число от 0 до 100. Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему, в какую сторону идти.

# import random
# n = random.randint(0,100)
# b = int(input('Guess number from 0 to 100 '))
# while b > n:
#   b = int(input('No. The hidden number is less ' ))
# while b < n:
#   b = int(input('No. The hidden number is greater '))
# else:
#   print('Yes! Congratulations!!!')


import random
n = random.randint(0,100)
while True:
    b = int(input('Guess number from 0 to 100 '))
    if b == n:
        print('Yes! Congratulations!!!')
        break
    elif b > n:
        print('No. The hidden number is less ')
    else:
        print('No. The hidden number is greater ')