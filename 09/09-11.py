list = []
for i in range(int(input())):
    list.append(input())
search = []
for j in range(int(input())):
    search.append(input())
for k in search:
    if k in list:
        print(k)