text = input()

emoticons = []

for i in range(len(text)):
    if text[i] == ':' and not (text[i + 1] == '.' or text[i + 1] == ',' or text[i + 1] == ' '):
        emoticon = text[i:i + 2]
        emoticons.append(emoticon)

print('\n'.join(emoticons))
