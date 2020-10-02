nums=input()
n=int(input())

list1=nums.split(' ')

for i in range(n):
    import sys
    min_num=sys.maxsize
    for el in list1:
        if int(el)<min_num:
            min_num=int(el)
    list1.remove(str(min_num))

list2=[]
for el in list1:
    list2.append(int(el))

print(list2)