n = int(input())
list = []
for i in range(n):
    word = input()
    list.append(word)
word1 = input()
for i in list:
    if word1 in i:
        print(i)