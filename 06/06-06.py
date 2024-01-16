M = int(input())
N = int(input())
library = set()
listbook = set()
for i in range(M):
    book = input()
    library.add(book)
for i in range(N):
    book = input()
    listbook.add(book)
    if book in library:
        print('YES')
    else:
        print('NO')