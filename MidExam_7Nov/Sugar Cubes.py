cubes_list = input().split()

command = input()

while not command == 'Mort':
    if command.find('Add') >= 0:
        word, value = command.split()
        cubes_list.append(value)
    elif command.find('Remove') >= 0:
        word, value = command.split()
        cubes_list.remove(value)
    elif command.find('Replace') >= 0:
        word, value, replace = command.split()
        if value in cubes_list:
            index1 = cubes_list.index(value)
            cubes_list[index1] = replace
    elif command.find('Collapse') >= 0:
        word, value = command.split()
        value = int(value)
        cubes_list = list(map(int, cubes_list))
        cubes_list = [el for el in cubes_list if el >= value]
    command = input()

print(' '.join(map(str, cubes_list)))
