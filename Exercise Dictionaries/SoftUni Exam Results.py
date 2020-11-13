languages = {}
usernames = {}

command = input()
while not command == 'exam finished':

    if 'banned' not in command:
        user, language, points = command.split('-')
        points = int(points)
        if user not in usernames:
            usernames[user] = []
        usernames[user].append(points)
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
    else:
        user, ban = command.split('-')
        if user in usernames:
            usernames.pop(user)

    command = input()

usernames_max = {key: max(value) for key, value in usernames.items()}
usernames_max = dict(sorted(usernames_max.items(), key=lambda x: (-x[1], x[0])))
languages = dict(sorted(languages.items(), key=lambda x: (-x[1], x[0])))

print(f'Results:')
for key, value in usernames_max.items():
    print(f'{key} | {value}')

print(f'Submissions:')
for key, value in languages.items():
    print(f'{key} - {value}')
