M = int(input())
N = int(input())
english = set()
german = set()
for i in range(M):
    student = input()
    english.add(student)
for i in range(N):
    student = input()
    german.add(student)
onelanguage = english ^ german
if len(onelanguage):
    print(len(onelanguage))
else:
    print('NO')