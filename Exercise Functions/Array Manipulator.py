def str_to_list(string):
    list1 = string.split()
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    return list1


def exchange(list1, index):
    count = 0
    if index > len(list1):
        print('Invalid index')
    while count < index + 1:
        list1.append(list1[0])
        list1.pop(0)
        count += 1
    return list1


def min_max_even_odd(list1, par):
    import sys
    max_num = -sys.maxsize
    min_num = sys.maxsize
    count = 0
    if par == 'max even':
        for i in range(len(list1)):
            if list1[i] % 2 == 0 and list1[i] > max_num:
                count += 1
                max_num = list1[i]
                index = i
            if list1[i] % 2 == 0 and list1[i] == max_num:
                max_num = list1[i]
                index = i
        if count == 0:
            return 'No matches'
        else:
            return index
    if par == 'max odd':
        for i in range(len(list1)):
            if not list1[i] % 2 == 0 and list1[i] > max_num:
                max_num = list1[i]
                index = i
            if not list1[i] % 2 == 0 and list1[i] == max_num:
                max_num = list1[i]
                index = i
        if count == 0:
            return 'No matches'
        else:
            return index
    if par == 'min even':
        for i in range(len(list1)):
            if list1[i] % 2 == 0 and list1[i] < min_num:
                min_num = list1[i]
                index = i
            if list1[i] % 2 == 0 and list1[i] == min_num:
                min = list1[i]
                index = i
        if count == 0:
            return 'No matches'
        else:
            return index
    if par == 'min odd':
        for i in range(len(list1)):
            if not list1[i] % 2 == 0 and list1[i] < min_num:
                min_num = list1[i]
                index = i
            if not list1[i] % 2 == 0 and list1[i] == min_num:
                min = list1[i]
                index = i
        if count == 0:
            return 'No matches'
        else:
            return index


def first_last_even_odd(list1, par):
    li = []
    word1, value, word2 = par.split()
    value = int(value)
    if value > len(list1):
        return 'Invalid count'
    if word1 == 'first' and word2 == 'even':
        for i in range(len(list1)):
            if list1[i] % 2 == 0 and value > 0:
                li.append(list1[i])
                value -= 1
        return li
    if word1 == 'first' and word2 == 'odd':
        for i in range(len(list1)):
            if not list1[i] % 2 == 0 and value > 0:
                li.append(list1[i])
                value -= 1
        return li
    if word1 == 'last' and word2 == 'even':
        for i in range(len(list1) - 1, -1, -1):
            if list1[i] % 2 == 0 and value > 0:
                li.insert(0, list1[i])
                value -= 1
        return li
    if word1 == 'last' and word2 == 'odd':
        for i in range(len(list1) - 1, -1, -1):
            if not list1[i] % 2 == 0 and value > 0:
                li.insert(0, list1[i])
                value -= 1
        return li

list1=str_to_list(input())
line=None
while line!='end':
    line=input()
    if 'exchange' in line:
        word,value=line.split()
        value=int(value)
        if value > len(list1):
            print('Invalid index')
        list1=exchange(list1,value)
    if 'max ' or 'min' in line:
        print(min_max_even_odd(list1,line))
    if 'first' or 'last' in line:
        print(first_last_even_odd(list1,line))