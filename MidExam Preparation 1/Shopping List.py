def urgent(list1, item):
    if item in list1:
        return list1
    list1.insert(0, item)
    return list


def unnecessary(list1, item):
    if item in list1:
        list1.remove(item)
        return list1
    return list1


def correct(list1, old_item, new_item):
    if old_item in list1:
        index1 = list1.index(old_item)
        list1[index1] = new_item
        return list1
    return list1


def rearrange(list1, item):
    if item in list1:
        list1.remove(item)
        list1.append(item)
        return list1
    return list1


grocery_list1 = input().split('!')
line = input()

while line != 'Go Shopping!':

    if line.find('Urgent')>=0:
        command, item = line.split()
        urgent(grocery_list1, item)
    elif line.find('Unnecessary')>=0:
        command, item = line.split()
        unnecessary(grocery_list1, item)
    elif line.find('Correct')>=0:
        command, oldItem, newItem = line.split()
        correct(grocery_list1, oldItem, newItem)
    elif line.find('Rearrange')>=0:
        command, item = line.split()
        rearrange(grocery_list1, item)
    line = input()

print(', '.join(grocery_list1))