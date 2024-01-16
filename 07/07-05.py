word1 = str(input())
word2 = str(input())
while word1[-1] == word2[0]:
    word = str(input())
    if word[-1] == word2[0]:
        word2 = str(input())
    else:
        print(word)
        break