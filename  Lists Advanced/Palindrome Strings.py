def find_the_palin(string, search):
    count = 0
    list_palin = []
    list1 = string.split()
    for el in list1:
        if search == el:
            count += 1
        if el == el[::-1]:
            list_palin.append(el)
    return list_palin, count


str_line = input()
searched_palin = input()
result=find_the_palin(str_line,searched_palin)
print(result[0])
print(f'Found palindrome {result[1]} times')