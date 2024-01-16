list = []
for i in range(int(input())):
 list.append(input())
list2 = []
for i in range(int(input())):
 n = int(input())
 list2.append(list[n - 1])
print('\n'.join(list2))