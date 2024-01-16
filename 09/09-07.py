flag = False
n = int(input())
list = []
for i in range(n):
    word = input()
    list.append(word)
m = int(input())
list1 = []
for i in range(m):
    words = input()
    list1.append(words)
for i in list:
    flag = True
    for j in list1:
        if j not in i:
            flag = False
    if flag:
        print(i)
