M = int(input())
n = int(input())
all = set(input() for i in range(n))
for i in range(1, M):
    list = set(input() for i in range(n))
    all &= list
for name in all:
    print(name)