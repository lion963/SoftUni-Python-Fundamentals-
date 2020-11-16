contests = {}

line = input()
while not line == 'end of contests':
    contest, password = line.split(':')
    if contest not in contests:
        contests[contest] = password
    else:
        contests[contest] = password
    line = input()

users = {}

line = input()
while not line == 'end of submissions':
    contest1, password1, user, point = line.split('=>')
    point = int(point)
    if (contest1 in contests) and (password1 == contests[contest1]):
        if user not in users:
            users[user] = {contest1: point}
        else:
            if contest1 in users[user]:
                if users[user][contest1] < point:
                    users[user][contest1] = point
            else:
                users[user].update({contest1: point})
    line = input()

sum1 = 0
max_sum = 0
for key, value in users.items():
    for key1, value1 in value.items():
        sum1 += value1
    if sum1 > max_sum:
        max_sum = sum1
        name = key
    sum1 = 0
print(f'Best candidate is {name} with total {max_sum} points.')

print('Ranking:')
for key, value in sorted(users.items(), key=lambda x: x[0]):
    print(f'{key}')
    for contest2, point2 in sorted(value.items(), key=lambda x: -x[1]):
        print(f'#  {contest2} -> {point2}')
