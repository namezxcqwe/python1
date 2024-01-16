num = int(input('Введите кол-во секунд, оставшиеся до запуска: '))
if num < 0:
    print('Пуск')
for i in range(num, -1, -1):
    if i == 0:
        print('Пуск')
    else:
        print('Осталось секунд: ', i)