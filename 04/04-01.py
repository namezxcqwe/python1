days = 0
t = float(input('Введите температуру за 1 день: '))
while t < 22:
    days += 1
    t = float(input('Введите температуру за 1 день: '))
print(days // 7)