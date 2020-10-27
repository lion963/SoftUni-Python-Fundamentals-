def shoot(list1, index_shoot, value_reduce):
    if 0 <= index_shoot < len(list1):
        list1[index_shoot] -= value_reduce
        if list1[index_shoot] <= 0:
            list1.pop(index_shoot)
    return list1


def add(list1, index_add, value_add):
    if 0 <= index_add < len(list1):
        list1.insert(index_add, value_add)
    else:
        print(f'Invalid placement!')
    return list1


def strike(list1, index_strike, radius_strike):
    left_index = index_strike - radius_strike
    rigth_index = index_strike + radius_strike
    if left_index >= 0 and rigth_index < len(list1):
        left_part = list1[:left_index]
        rigth_part = list1[rigth_index + 1:]
        list1 = left_part + rigth_part
    else:
        print(f'Strike missed!')
    return list1


targets = list(map(int, input().split()))
line = input()

while not line == 'End':
    command, index, value = line.split(' ')
    index = int(index)
    value = int(value)

    if command == 'Shoot':
        targets = shoot(targets, index, value)
    elif command == 'Add':
        targets = add(targets, index, value)
    elif command == 'Strike':
        targets = strike(targets, index, value)

    line = input()

print('|'.join(map(str, targets)))