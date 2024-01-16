first = set()
second = set()
while True:
    number = input()
    if number == '':
        break
    first.add(number)
while True:
    number = input()
    if number == '':
        break
    second.add(number)
intersection = first & second
if intersection:
    for i in intersection:
        print(i)
else:
    print('EMPTY')