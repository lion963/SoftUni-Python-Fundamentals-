usernames = input().split(', ')

valid_usernames = []

for user in usernames:
    counter = 0
    if 3 <= len(user) <= 16:
        for ch in user:
            if ch.isdigit() or ch.isalpha() or ch == '-' or ch == '_':
                counter += 1
            if counter == len(user):
                valid_usernames.append(user)

for user in valid_usernames:
    print(user)
