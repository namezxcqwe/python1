n = int(input())
list = []
for i in range(n):
    num = input()
    list.append(num)
list.sort()
for k in range(len(list)):
    print(list[k])