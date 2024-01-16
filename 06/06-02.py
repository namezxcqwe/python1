n = int(input())
city = input()
list = set()
for _ in range(n):
    city = input()
    list.add(city)
if city in list:
    print('TRY ANOTHER')
else:
    print('OK')