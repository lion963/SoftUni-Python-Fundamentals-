def validation(list_of_indexes, list1):
    RANGE1 = range(0, len(list1))
    if list_of_indexes[0] == list_of_indexes[1] or list_of_indexes[0] not in RANGE1 or list_of_indexes[1] not in RANGE1:
        return False
    return True


def add_elements(number, list1):
    print(f'Invalid input! Adding additional elements to the board')
    add_el = str(-number) + 'a'
    list1.insert(len(list1) // 2, add_el)
    list1.insert(len(list1) // 2, add_el)
    return list1


def remove(list_of_indexes, list1):
    if list1[list_of_indexes[0]] == list1[list_of_indexes[1]]:
        print(f'Congrats! You have found matching elements - {list1[list_of_indexes[0]]}!')
        list1[list_of_indexes[0]] = 'remove'
        list1[list_of_indexes[1]] = 'remove'
        list1.remove('remove')
        list1.remove('remove')
        return list1
    print('Try again!')
    return list1


sequence_of_el = input().split()

line = input()
moves = 0

while not line == 'end':
    indexes = list(map(int, line.split()))

    if validation(indexes, sequence_of_el):
        moves += 1
        remove(indexes, sequence_of_el)
    else:
        moves += 1
        add_elements(moves, sequence_of_el)

    if len(sequence_of_el) == 0:
        print(f'You have won in {moves} turns!')
        break

    line = input()

if len(sequence_of_el) > 0:
    print(f'Sorry you lose :(')
    print(' '.join(sequence_of_el))