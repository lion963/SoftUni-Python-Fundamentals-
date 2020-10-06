def palindrome(string):
    list1 = string.split(', ')
    for el in list1:
        list2 = list(el)
        list3 = list(el)
        list3.reverse()
        if list2 == list3:
            print(True)
        else:
            print(False)


palindrome(input())