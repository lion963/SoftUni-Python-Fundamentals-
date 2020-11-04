def Include(list1, element):
    list1.append(element)
    return list1


def Visit(list1, first_or_last, num):
    if num in range(len(list1)+1):
        if first_or_last == 'first':
            list1 = list1[num:]
            return list1
        elif first_or_last == 'last':
            list1 = list1[:len(list1) - num]
            return list1
    return list1


def Prefer(list1, index_1, index_2):
    if index_1 in range(len(list1)) and index_2 in range(len(list1)):
        list1[index_1], list1[index_2] = list1[index_2], list1[index_1]
        return list1
    return list1


def Place(list1, element, index_to_place):
    if index_to_place in range(len(list1)):
        list1.insert(index_to_place + 1, element)
        return list1
    return list1


shops_list = input().split()
num_of_commands = int(input())

count=1

while count<=num_of_commands:
    command = input()

    if command.find('Include') >= 0:
        word, shop = command.split()
        shops_list = Include(shops_list, shop)
    elif command.find('Visit') >= 0:
        word, first_last, num_shops = command.split()
        num_shops = int(num_shops)
        shops_list = Visit(shops_list, first_last, num_shops)
    elif command.find('Prefer') >= 0:
        word, index1, index2 = command.split()
        index1 = int(index1)
        index2 = int(index2)
        shops_list = Prefer(shops_list, index1, index2)
    elif command.find('Place') >= 0:
        word, shop, shop_index = command.split()
        shop_index = int(shop_index)
        shops_list = Place(shops_list, shop, shop_index)
    count+=1

print(f'Shops left:\n{" ".join(shops_list)}')
