import random
n = random.randint(1,5)
b = int(input('Guess number from 1 to 5 '))
while b != n:
    b = int(input('No, try again ' ))
else:
    print('Yes! Congratulations!!!')