def swap(list1, index_1, index_2):
    list1[index_1], list1[index_2] = list1[index_2], list1[index_1]
    return list1


def multiply(list1, index_1, index_2):
    list1[index_1] = list1[index_1] * list1[index_2]
    return list1


def decrease(list1):
    list1 = [el - 1 for el in list1]
    return list1


number_list = list(map(int, input().split()))
command = input()

while not command == 'end':
    if command.find('swap') >= 0:
        word, index1, index2 = command.split()
        index1=int(index1)
        index2=int(index2)
        number_list = swap(number_list, index1, index2)
    elif command.find('multiply') >= 0:
        word, index1, index2 = command.split()
        index1 = int(index1)
        index2 = int(index2)
        number_list = multiply(number_list, index1, index2)
    else:
        number_list = decrease(number_list)
    command = input()

number_list = list(map(str, number_list))
print(', '.join(number_list))
