banned_words = input().split(', ')
text = input()

for word in banned_words:
    while word in text:
        text = text.replace(word, '*' * len(word))
print(text)

# word1, word2 = input().split(', ')
# text = input()
#
# text = text.replace(word1, (len(word1) * '*'))
# text = text.replace(word2, (len(word2) * '*'))
#
# print(text)
