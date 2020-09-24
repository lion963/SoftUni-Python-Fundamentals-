n = int(input())
check = None
count = 0

for i in range(1, n + 1):
    line = input()
    for char in range(len(line)):
        if ord(line[char]) == 40:
            check = 'open'
            count += 1
        if ord(line[char]) == 41:
            if check == 'open' and count == 1:
                check = 'close'
                count = 0
if check == 'close':
    print('BALANCED')
else:
    print('UNBALANCED')

# n = int(input())
# check = None
# count = 0
#
# for i in range(1, n + 1):
#     line = input()
#     if line == "(":
#         check = 'open'
#         count += 1
#     if line == ")":
#         if check == 'open' and count == 1:
#             check = 'close'
#             count = 0
#
# if check == 'close':
#     print('BALANCED')
# else:
#     print('UNBALANCED')
