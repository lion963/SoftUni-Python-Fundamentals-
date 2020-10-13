def add_last_wagon(string, data):
    word, people = string.split()
    people = int(people)
    people=data[-1]+people
    data.pop(-1)
    data.append(people)
    return data


def insert_index_wagon(string, data):
    word, index, people = string.split()
    index = int(index)
    people = int(people)
    people = data[index] + people
    data.pop(index)
    data.insert(index, people)
    return data


def remove_index_wagon(string, data):
    word, index, people = string.split()
    index = int(index)
    people = int(people)
    people = data[index] - people
    data.pop(index)
    data.insert(index, people)
    return data


n = int(input())
list1 = []
for i in range(n):
    list1.append(0)

command = input()

while command != 'End':

    if command.find('add') >= 0:
        list1 = add_last_wagon(command, list1)
    if command.find('insert') >= 0:
        list1 = insert_index_wagon(command, list1)
    if command.find('leave') >= 0:
        list1 = remove_index_wagon(command, list1)

    command = input()

print(list1)