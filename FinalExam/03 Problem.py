capacity = int(input())

users = {}

line = input()
while not line == 'Statistics':
    command_line = line.split('=')
    if command_line[0] == 'Add':
        username = command_line[1]
        sent = int(command_line[2])
        received = int(command_line[3])
        if username not in users:
            users[username] = {'sent': sent, 'received': received}
    elif command_line[0] == 'Message':
        sender = command_line[1]
        receiver = command_line[2]
        if sender in users and receiver in users:
            users[sender]['sent'] += 1
            users[receiver]['received'] += 1
            if (users[sender]['sent'] + users[sender]['received']) >= capacity:
                users.pop(sender)
                print(f'{sender} reached the capacity!')
            if (users[receiver]['sent'] + users[receiver]['received']) >= capacity:
                users.pop(receiver)
                print(f'{receiver} reached the capacity!')
    elif command_line[0] == 'Empty':
        username = command_line[1]
        if username in users:
            users.pop(username)
        if username == 'All':
            users = {}
    line = input()

if users:
    users = dict(sorted(users.items(), key=lambda x: (-x[1]['received'], x[0])))

print(f'Users count: {len(users)}')
for user, value in users.items():
    print(f"{user} - {value['sent'] + value['received']}")
