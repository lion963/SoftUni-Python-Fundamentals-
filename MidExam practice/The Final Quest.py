def delete_word(list1, index_1):
    if index_1 + 1 in range(len(list1)):
        list1.pop(index_1 + 1)
        return list1
    return list1


def swap_words(list1, word_1, word_2):
    if (word_1 and word_2) in list1:
        index1 = list1.index(word_1)
        index2 = list1.index(word_2)
        list1[index1], list1[index2] = list1[index2], list1[index1]
        return list1
    return list1


def put_word(list1, word_to_put, index_1):
    if index_1 - 1 in range(len(list1) + 1):
        list1.insert(index_1 - 1, word_to_put)
        return list1
    return list1


def sort_words(list1):
    list1.sort(reverse=True)
    return list1


def replace_words(list1, word_1, word_2):
    if word_2 in list1:
        index_of_word2 = list1.index(word2)
        list1[index_of_word2] = word_1
        return list1
    return list1


list_of_word = input().split()

command = input()

while not command == 'Stop':
    if command.find('Delete') >= 0:
        word, index1 = command.split()
        index1 = int(index1)
        list_of_word = delete_word(list_of_word, index1)
    elif command.find('Swap') >= 0:
        word, word1, word2 = command.split()
        list_of_word = swap_words(list_of_word, word1, word2)
    elif command.find('Put') >= 0:
        word, word_put, index1 = command.split()
        index1 = int(index1)
        list_of_word = put_word(list_of_word, word_put, index1)
    elif command.find('Sort') >= 0:
        list_of_word = sort_words(list_of_word)
    elif command.find('Replace') >= 0:
        word, word1, word2 = command.split()
        list_of_word = replace_words(list_of_word, word1, word2)
    command = input()

print(' '.join(list_of_word))
