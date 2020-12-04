message = input()

line = input()
while not line == 'Reveal':
    command_list = line.split(':|:')

    if command_list[0] == 'InsertSpace':
        index1 = int(command_list[1])
        message = message[:index1] + ' ' + message[index1:]
        print(message)
    elif command_list[0] == 'Reverse':
        substring = command_list[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print('error')
    elif command_list[0] == 'ChangeAll':
        substring1 = command_list[1]
        replacement = command_list[2]
        message = message.replace(substring1, replacement)
        print(message)

    line = input()

print(f'You have a new text message: {message}')
