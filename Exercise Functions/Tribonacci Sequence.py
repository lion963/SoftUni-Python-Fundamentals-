n=int(input())

list1=[0,0,1]

for i in range (1,n):
    tribonacci=list1[-1]+list1[-2]+list1[-3]
    list1.append(tribonacci)
list1.pop(0)
list1.pop(0)
list1=list(map(str,list1))
print(' '.join(list1))


# n=int(input())
#
# list1=[1]
# list2=[0,0,1]
#
# for i in range (1,n):
#     tribonacci=sum(list2)
#     list1.append(tribonacci)
#     list2.append(tribonacci)
#     list2.pop(0)
#
# list1=list(map(str,list1))
# print(' '.join(list1))