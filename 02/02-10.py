number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))
operation = input('Введите математическую операцию (+, -, * или /): ')
if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    if operation != 0:
        print(number1 / number2)
    else:
        print('888888')
else:
    print('888888')