list1=input().split(', ')

count=0
list2=[]

for el in list1:
    if el=='0':
        count+=1
    else:
        list2.append(int(el))

for i in range(count):
    list2.append(0)

print(list2)