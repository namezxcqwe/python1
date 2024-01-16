n = int(input())
list = []
list2 = []
for i in range(n):
    word = input()
    list.append(word)
nature = int(input())
for i in list:
    if nature > len(i):
        continue
    print(i[nature - 1])