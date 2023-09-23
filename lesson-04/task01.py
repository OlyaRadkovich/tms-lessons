s = 0
for num in range(1, 101):
    s += num
print(f'{1}:{s}')

s = 0
for num in range(100, 1001):
    s += num
print(f'{2}:{s}')

s = 0
for num in range(100, 1001):
    if num % 2 == 0:
        s += num
print(f'{3}:{s}')

m = 1
for num in range (1,11):
   m *=num
print(f'{4}:{m}')

m = 1
for num in range(10):
   m *= 2
print(f'{5}:{m}')

sum = 0
for i in range(0,100):
    sum += i
    if sum < 1000:
        continue
    else:
        print(f'{6}:{sum}, {i}')
        break


