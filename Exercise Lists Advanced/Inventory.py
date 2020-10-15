items=input().split(', ')

command=input()

while not command=='Craft!':

    if command.find('Collect')>=0:
        word, item=command.split(' - ')
        if item not in items:
            items.append(item)
    elif command.find('Drop')>=0:
        word, item = command.split(' - ')
        if item in items:
            items.remove(item)
    elif command.find('Combine')>=0:
        word1, word2 = command.split(' - ')
        item = word2.split(':')
        for i in range(len(items)):
            if items[i] == item[0]:
                items.insert(i + 1, item[1])
    elif command.find('Renew')>=0:
        word, item = command.split(' - ')
        if item in items:
            items.remove(item)
            items.append(item)
    command = input()

items=', '.join(items)
print(items)