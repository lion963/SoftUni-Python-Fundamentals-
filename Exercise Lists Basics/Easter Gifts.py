str1=input()

list1=str1.split(' ')
line=''

while line!='No Money':
    line=input()
    if line=='No Money':
        break
    line.split(' ')

    if 'OutofStock' in line:
        for el in list1:
            if el==line[1]:
                el='None'

    if 'Required' in line:
        for el in list1:
            if el=='None':
                list1.remove(el)
        if int(line[2])>=len(list1)-1:
            list1.pop(int(line[2]))
            list1.insert(int(line[2]),line[1])

    if 'JustInCase' in line:
        list1.pop(len(list1)-1)
        list1.append(line[1])

print(list1)