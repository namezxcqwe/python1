n = int(input())
list = []
for i in range(n):
    eat = input()
    if 'лук' not in eat:
        list.append(eat)
print(', '.join(list))
