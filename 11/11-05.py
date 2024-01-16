s = input().split()
print(str('[' + ', '.join('"' + s[i] + '"' for i in range(len(s))) + ']'))
