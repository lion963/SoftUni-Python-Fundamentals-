activation_key = input()

line = input()
while not line == 'Generate':
    command_list = line.split('>>>')

    if command_list[0] == 'Contains':
        sub_str = command_list[1]
        if sub_str in activation_key:
            print(f'{activation_key} contains {sub_str}')
        else:
            print(f'Substring not found!')
    elif command_list[0] == 'Flip':
        command = command_list[1]
        start_index = int(command_list[2])
        end_index = int(command_list[3])
        str1 = activation_key[start_index:end_index]
        if command == 'Lower':
            str1 = activation_key[start_index:end_index].lower()
            activation_key = activation_key[:start_index] + str1 + activation_key[end_index:]
        elif command == 'Upper':
            str1 = activation_key[start_index:end_index].upper()
            activation_key = activation_key[:start_index] + str1 + activation_key[end_index:]
        print(activation_key)
    elif command_list[0] == 'Slice':
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    line = input()

print(f'Your activation key is: {activation_key}')
