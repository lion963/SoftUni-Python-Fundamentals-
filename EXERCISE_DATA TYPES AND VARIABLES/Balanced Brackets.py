n = int(input())
check = 'ok'
count = 0
condit=False

for i in range(1, n + 1):
    line = input()
    if condit==True:
        break
    for char in range(len(line)):
        if ord(line[char]) == 40:
            check = 'open'
            count += 1
        if ord(line[char]) == 41:
            if check=='ok':
                condit=True
                break
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
#         if check==None:
#             break
#         if check == 'open' and count == 1:
#             check = 'close'
#             count = 0
#
# if check == 'close':
#     print('BALANCED')
# else:
#     print('UNBALANCED')
