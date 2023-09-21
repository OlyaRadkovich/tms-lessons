num = int(input('Enter a number . If  it is prime, the program will output "True", if not - "False" '))
if num <= 1:
    print('False. Prime numbers start with 2. Google for details ')
else:
    i = 2
    for i in range(2, num):
        if (num % i) != 0:
            i +=1
        else:
            break
print(num % i == 0 and i == num)


# Не знаю, как исправить ошибку, которая появляется, если ввести 1 или что-то меньше.