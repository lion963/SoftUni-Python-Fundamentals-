def move(string, n):
    new_string = string[n:] + string[:n]
    return new_string


def insert(string, index, value):
    new_string = string[:index] + value + string[index:]
    return new_string


def change_all(string, substr, replacement):
    new_string = string.replace(substr, replacement)
    return new_string


message = input()

command = input()
while not command == 'Decode':
    if 'Move' in command:
        word, num = command.split('|')
        num = int(num)
        message = move(message, num)
    elif 'Insert' in command:
        word, index1, value1 = command.split('|')
        index1 = int(index1)
        message = insert(message, index1, value1)
    elif 'ChangeAll' in command:
        word, substr1, replacement1 = command.split('|')
        message = change_all(message, substr1, replacement1)
    command = input()
print(f'The decrypted message is: {message}')
