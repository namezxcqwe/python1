word = input()
n = int(input())
if n <= len(word):
    print(word[n - 1])
else:
    print("ОШИБКА")