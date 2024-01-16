password1 = input('Введите свой пароль: ')
password2 = input('Подтвердите введённый пароль: ')
while password1 == password2 and len(password1) <= 8 :
    print('Короткий')
    password1 = input('Введите свой пароль: ')
    password2 = input('Подтвердите введённый пароль: ')
while password1 != password2 and len(password1):
    print('Различаются')
    password1 = input('Введите свой пароль: ')
    password2 = input('Подтвердите введённый пароль: ')
while password1 == password2 and len(password1) > 8:
    print('OK')