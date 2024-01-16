n = int(input())
name = [input() for i in range(n)]
k = int(input())
m = int(input())
for j in range(m):
    del name[k - 1::k]
print('\n'.join(name))