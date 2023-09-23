import random
n = random.randint(0,100)
b = int(input('Guess number from 0 to 100 '))
while b > n:
    b = int(input('No. The hidden number is less ' ))
while b < n:
    b = int(input('No. The hidden number is greater '))
else:
    print('Yes! Congratulations!!!')