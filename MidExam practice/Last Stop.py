list_of_painting = input().split()

command = input()

while not command == 'END':
    if command.find('Change') >= 0:
        word, first_num, second_num = command.split()
        if first_num in list_of_painting:
            index1 = list_of_painting.index(first_num)
            list_of_painting[index1] = second_num
    elif command.find('Hide') >= 0:
        word, paint_num = command.split()
        if paint_num in list_of_painting:
            list_of_painting.remove(paint_num)
    elif command.find('Switch') >= 0:
        word, paint_num1, paint_num2 = command.split()
        if (paint_num1 and paint_num2) in list_of_painting:
            index_1 = list_of_painting.index(paint_num1)
            index_2 = list_of_painting.index(paint_num2)
            list_of_painting[index_1], list_of_painting[index_2] = list_of_painting[index_2], list_of_painting[
                    index_1]
    elif command.find('Insert') >= 0:
        word, place, paint_num = command.split()
        place = int(place)
        if place+1 in range(len(list_of_painting)+1):
            list_of_painting.insert(place + 1, paint_num)
    elif command.find('Reverse') >= 0:
        list_of_painting=list_of_painting[::-1]
    command = input()
print(' '.join(list_of_painting))
