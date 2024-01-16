list = []
list1 = []
n = int(input())
for i in range(n):
    family = input()
    if "5" in line or "4" in family:
        list.append(family)
        list1.append(family)
    else:
        list1.append(family)
        continue
for j in range(len(list1)):
    print(list1[j])
print()
for k in range(len(list)):
    print(list[k])