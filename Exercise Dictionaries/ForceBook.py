force_book_dict = {}

command = input()
while not command == 'Lumpawaroo':

    if '|' in command:
        flag = False
        side, user = command.split(' | ')
        if side not in force_book_dict:
            force_book_dict[side] = []
        for value in force_book_dict.values():
            if user in value:
                flag = True
        if not flag:
            force_book_dict[side].append(user)

    if '-' in command:
        user, side = command.split(' -> ')
        for value in force_book_dict.values():
            if user in value:
                value.remove(user)
        force_book_dict[side].append(user)
        print(f'{user} joins the {side} side!')

    command = input()

force_book_dict = dict(sorted(force_book_dict.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in force_book_dict.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for el in sorted(value):
            print(f'! {el}')


# command = input()
#
# users = {}
# result = {}
# while command != "Lumpawaroo":
#     if len(command.split(" | ")) == 2:
#         value, key = command.split(" | ")
#
#         if key not in users:
#             users[key] = value
#
#     elif len(command.split(" -> ")) == 2:
#         key, value = command.split(" -> ")
#
#         users[key] = value
#
#         print(f"{key} joins the {value} side!")
#
#     command = input()
#
# for key, value in users.items():
#     if value not in result:
#         result[value] = []
#         result[value].append(key)
#
#     else:
#         result[value].append(key)
#
# result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))
# for key, value in result.items():
#     print(f"Side: {key}, Members: {len(value)}")
#     [print(f"! {name}") for name in sorted(value)]
