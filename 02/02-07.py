a = float(input('Введите любое число: '))
if (a < 10 ** -6) or a == 0:
    print(1000000)
else:
    print(a ** -1)