city1 = input('Введите первый город: ')
city2 = input('Введите второй город: ')
if city1 == city2 or city1 == 'Тула' and city2 == 'Пенза' or city1 == 'Пенза' and city2 == 'Тула':
    print('Нет')
elif city1 != city2 or city1 == 'Тула' and city2 != 'Пенза' or city1 == 'Пенза' and city2 != 'Тула':
    print('Да')