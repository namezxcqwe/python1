n = int(input('Введите натуральное число: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    result = 'ПРОСТОЕ'
else:
    result = 'НЕТ'
print(result)