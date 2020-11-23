line = input()

current_result = ''
result = ''

index = 0

while index < len(line):
    if not line[index].isdigit():
        current_result += line[index]
        index += 1
    else:
        number = ''
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1
        number = int(number)
        current_result = current_result.upper() * number
        result += current_result
        current_result = ''

print(f"Unique symbols used: {len(set(result))}")
print(result)

# symbols = input()
#
# symbols_dict = {}
# rage_message = ''
# key_str = ''
# unique_list = []
#
# while not symbols == '':
#     str1 = ''
#     number = ''
#     for i in range(len(symbols)):
#         if not symbols[i].isdigit():
#             str1 += symbols[i].upper()
#         else:
#             number += symbols[i]
#             if i == len(symbols) - 1:
#                 number = int(number)
#                 symbols = ''
#                 break
#             elif not symbols[i + 1].isdigit():
#                 number = int(number)
#                 symbols = symbols[i + 1:]
#                 break
#     symbols_dict[str1] = number
#
# for key, value in symbols_dict.items():
#     rage_message += key * value
#     key_str += key
#
# for el in key_str:
#     if el not in unique_list and not el == ' ':
#         unique_list.append(el)
#
# print(f'Unique symbols used: {len(unique_list)}')
# print(rage_message)
