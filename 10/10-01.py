n = int(input())
list = []
f = 0
for i in range(n):
    m = int(input())
    list.append(m)
sum = int(input())
for i in range(n):
    for k in range(i + 1, n):
        if sum == list[i] * list[k]:
            f = 1
if f == 1:
    print("ДА")
else:
    print("НЕТ")