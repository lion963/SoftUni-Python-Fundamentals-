str1=input()

list1=str1.split(' ')
line=''

while line!='No Money':
    line=input()
    if line=='No Money':
        break
    line1=line.split(' ')

    if 'OutOfStock' in line1:
        for i in range(len(list1)):
            if list1[i]==line1[1]:
                list1.remove(list1[i])
                list1.insert(i,'None')

    if 'Required' in line1:
        if int(line1[2])<=len(list1)-1:
            list1.pop(int(line1[2]))
            list1.insert(int(line1[2]),line1[1])

    if 'JustInCase' in line1:
        list1.pop(len(list1)-1)
        list1.append(line1[1])

for el in list1:
    if el=='None':
        list1.remove(el)

str2=' '.join(list1)
print(str2)

# gifts = input().split(' ')
#
# command = input().split(' ')
# while command[0] != 'No' and command[1] != 'Money':
#     index = 0
#     if command[0] == 'OutOfStock':
#         gift = command[1]
#         gifts = list(map(lambda lst: lst.replace(gift, "None"), gifts))
#
#     elif command[0] == 'Required':
#         index = int(command[2])
#         if 0 < index < len(gifts):
#             gifts[index] = command[1]
#
#     elif command[0] == 'JustInCase':
#         gifts[-1] = command[1]
#
#     command = input().split(' ')
#
# while 'None' in gifts:
#     gifts.remove('None')
#
# for i in gifts:
#     print(i, end=' ')