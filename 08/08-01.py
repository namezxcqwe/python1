word1 = input()
mn = word1
mx = word1
while True:
    word2 = input()
    if word2 == 'стоп':
        break
    if len(word2) > len(mx):
        mx = word2
    if len(word2) < len(mn):
        mn = word2

if len(set(mn) -  set(mx)) == 0:
    print('Да')
else:
    print('Нет')