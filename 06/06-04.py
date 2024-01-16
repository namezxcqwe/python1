M = int(input())
N = int(input())
english = set()
german = set()
for i in range(M + N):
    student = input()
    if i < M:
        english.add(student)
    else:
        german.add(student)
onelanguage = english ^ german
if len(onelanguage):
    print(len(onelanguage))
else:
    print('NO')