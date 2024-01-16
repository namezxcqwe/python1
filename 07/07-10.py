step = int(input())
word = input()
for i in word:
   word1 = ord(i) + step
   if ord(i) < 1040 or ord(i) > 1103:
       print(i, end = '')
   elif 1072 <= ord(i) <= 1103:
       if word1 > 1103:
           print(chr(1072 + (word1 - 1104)), end = '')
       else:
           print(chr(word1), end = '')
   else:
       if word1 > 1071:
           print(chr(1040 + (word1 - 1072)), end = '')
       else:
           print(chr(word1), end = '')