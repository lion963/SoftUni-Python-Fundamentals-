str1=input()
n=int(input())

list1=str1.split(' ')
a=list1[0]
z=list1[len(list1)-1]

list1.pop(0)
list1.pop(len(list1)-1)

for i in range(n):
    list_left = list1[:len(list1) // 2]
    list_right = list1[len(list1) // 2:]
    list1=[]
    for index in range(len(list_left)):
        list1.append(list_right[index])
        list1.append(list_left[index])

list1.append(z)
list1.insert(0,a)

print(list1)