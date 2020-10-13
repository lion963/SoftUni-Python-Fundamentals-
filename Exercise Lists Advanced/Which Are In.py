list1 = input().split(', ')
list2 = input().split(', ')
list3 = []
list4=[]

for el in list1:
    for ele in list2:
        if ele.find(el) >= 0:
            list3.append(el)

for el in list1:
    if el in list3:
        list4.append(el)

print(list4)