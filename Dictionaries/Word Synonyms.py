n = int(input())

dict_synonyms = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in dict_synonyms:
        dict_synonyms[word] = []
    dict_synonyms[word].append(synonym)

for word in dict_synonyms:
    print(f"{word} - {', '.join(dict_synonyms[word])}")
