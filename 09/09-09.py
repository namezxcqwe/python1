n = int(input())
list = []
list1 = []
for i in range(n):
    sum = int(input())
    list.append(sum)
    list1.append(sum)
for i in range(n):
    list1[i] = list1[i] * 3
for i in range(n):
    print(list[i])
print()
for i in range(n):
    print(list1[i])