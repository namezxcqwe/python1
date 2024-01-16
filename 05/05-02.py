n = int(input('Введите кол-во строк: '))
for i in range(n):
    words = str(input('Введите свои слова/словосочетания/предложения: '))
if 'Кот' in words or 'кот' in words:
    print('Мяу!')
else:
    print('Нет')