def case(user_name, flag):
    if flag:
        user_name = user_name.lower()
    else:
        user_name = user_name.upper()
    return user_name


def reverse(user_name, start, stop):
    if stop == len(user_name) - 1:
        user = user_name[start:][::-1]
    else:
        user = user_name[start:stop + 1][::-1]
    return user


def cut(user_name, sub):
    if sub in user_name:
        user_name = user_name.replace(sub, '', 1)
        print(user_name)
        return user_name
    else:
        print(f"The word {user_name} doesn't contain {sub}.")
        return user_name


def replace(user_name, char):
    if char in user_name:
        user_name = user_name.replace(char, '*')
    return user_name


def check(user_name, char):
    if char in user_name:
        print('Valid')
    else:
        print(f'Your username must contain {char}.')


username = input()

line = input()
while not line == 'Sign up':
    command_lst = line.split()
    if command_lst[0] == 'Case':
        if command_lst[1] == 'lower':
            flag = True
        else:
            flag = False
        username = case(username, flag)
        print(username)
    elif command_lst[0] == 'Reverse':
        start_index = int(command_lst[1])
        end_index = int(command_lst[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username) and start_index < end_index:
            print(reverse(username, start_index, end_index))
    elif command_lst[0] == 'Cut':
        substring = command_lst[1]
        username = cut(username, substring)
    elif command_lst[0] == 'Replace':
        char = command_lst[1]
        username = replace(username, char)
        print(username)
    elif command_lst[0] == 'Check':
        char = command_lst[1]
        check(username, char)
    line = input()
