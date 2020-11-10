words = input().split()
dictionary_words = {}
odd_dictionary = {}

for word in words:
    word = word.lower()
    if word not in dictionary_words:
        dictionary_words[word] = 0
    dictionary_words[word] += 1

for (key, value) in dictionary_words.items():
    if not value % 2 == 0:
        odd_dictionary[key] = value

for key in odd_dictionary.keys():
    print(key, end=' ')
