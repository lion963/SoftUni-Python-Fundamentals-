str = input()

list2=[]


def new_list(string):
    li = []
    li[:0] = string
    return li


list1 = new_list(str)

for char in range(len(list1)):
    for i in range(65, 91):
        if ord(list1[char]) == i:
            list2.append(char)

print(list2)