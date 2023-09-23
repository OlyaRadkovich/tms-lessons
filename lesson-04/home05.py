n = int(input('Enter any number '))
sum = 0
while n != 0:
    sum += n % 10
    n //= 10
print(f'The sum of the digits of this number: {sum}')
