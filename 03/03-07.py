num1 = 1
num2 = 1001
print(num2 // 2)
symbol = str(input())
while symbol != '=':
    if symbol == '<':
        num2 = num2 - (num2 - num1) // 2
        x = num2 - (num2 - num1) // 2
    if symbol == '>':
        num1 = num1 + (num2 - num1) // 2
        x = num1 + (num2 - num1) // 2
    print(x)
    symbol = str(input())