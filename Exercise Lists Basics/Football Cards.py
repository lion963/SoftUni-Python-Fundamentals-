str1 = input()

condit = False

listA = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
listB = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

list_card = str1.split(' ')

for i in range(len(list_card)):
    if list_card[i] in listA:
        listA.remove(list_card[i])
    if list_card[i] in listB:
        listB.remove(list_card[i])
    if len(listA) < 7 or len(listB) < 7:
        condit = True
        break

print(f'Team A - {len(listA)}; Team B - {len(listB)}')
if condit:
    print(f'Game was terminated')
