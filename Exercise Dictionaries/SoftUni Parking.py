n = int(input())

data = {}

for i in range(n):

    line = input()
    list_of_line = line.split()
    command = list_of_line[0]
    username = list_of_line[1]
    if len(list_of_line) > 2:
        license_plate = list_of_line[2]

    if command == 'register':
        if username not in data:
            data[username] = license_plate
            print(f'{username} registered {data[username]} successfully')
        else:
            print(f'ERROR: already registered with plate number {data[username]}')
    elif command == 'unregister':
        if username in data:
            print(f'{username} unregistered successfully')
            data.pop(username)
        else:
            print(f'ERROR: user {username} not found')

for key, value in data.items():
    print(f'{key} => {value}')
