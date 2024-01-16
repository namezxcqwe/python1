login = input('Введите желаемый логин: ')
adress = input('Введите резервный адрес: ')
if '@' in login and '@' in adress:
    print('Некорректный логин')
elif not '@' in adress and not '@' in login :
    print('Некорректный адрес')
elif not '@' in login and '@' in adress:
    print('OK')
else:
    print('Некорретные логин и адрес')