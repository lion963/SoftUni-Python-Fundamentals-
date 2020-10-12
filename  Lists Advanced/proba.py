list1=[1,2,4,6,8]
list2=list(map(str, list1))
print(list2)
list3=list(map(int,list2))
print(list3)

list4=list3[::-1]
print(list4)

