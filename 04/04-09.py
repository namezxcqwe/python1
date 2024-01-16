num = int(input('Введите высоту пирамиды: '))
for i in range(1, num + 1, 1):
    print(' ' * (num - i), '*' * (2 * i - 1))