def add_book(list1, book_name):
    list1.insert(0, book_name)
    return list1


def take_book(list1, book_name):
    list1.remove(book_name)
    return list1


def swap_books(list1, book_name1, book_name2):
    name1_index = list1.index(book_name1)
    name2_index = list1.index(book_name2)
    list1[name1_index], list1[name2_index] = list1[name2_index], list1[name1_index]
    return list1


def insert_book(list1, book_name):
    list1.append(name)
    return list1


def check_book(list1, index):
    if index <= len(list1) - 1:
        print(list1[index])


book_list = list(input().split('&'))
command = input()

while command != 'Done':
    if command.find('Add Book') >= 0:
        word, name = command.split(' | ')
        if name not in book_list:
            add_book(book_list, name)
    elif command.find('Take Book')>=0:
        word, name = command.split(' | ')
        if name in book_list:
            take_book(book_list, name)
    elif command.find('Swap Books') >= 0:
        word, name1, name2 = command.split(' | ')
        if name1 in book_list and name2 in book_list:
            swap_books(book_list, name1, name2)
    elif command.find('Insert Book') >= 0:
        word, name = command.split(' | ')
        insert_book(book_list, name)
    elif command.find('Check Book') >= 0:
        word, index1 = command.split(' | ')
        index1 = int(index1)
        check_book(book_list, index1)

    command = input()

print(', '.join(book_list))