str=input()


def str_to_list(string):
    li=list(string.split(', '))
    return li


list1=str_to_list(str)
for char in range(len(list1)):
    if list1[char]=='wolf' and char==(len(list1)-1):
        print(f'Please go away and stop eating my sheep')
    if list1[char]=='wolf' and not char==(len(list1)-1):
        print(f'Oi! Sheep number {(len(list1)-1)-char}! You are about to be eaten by a wolf!')