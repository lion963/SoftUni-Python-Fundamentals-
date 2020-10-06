RANGE1 = range(65, 90)
RANGE2 = range(97, 122)
RANGE3 = range(48, 57)


def password(string):
    list1 = list(string)
    count = 0
    condit = False
    if not 6 <= len(string) <= 10:
        print(f'Password must be between 6 and 10 characters')
    for el in list1:
        if ord(el) not in RANGE1 and ord(el) not in RANGE2 and ord(el) not in RANGE3:
            condit = True
        if ord(el) in RANGE3:
            count += 1
    if condit:
        print(f'Password must consist only of letters and digits')
    if count < 2:
        print(f'Password must have at least 2 digits')
    if not condit and count >= 2 and 6 <= len(string) <= 10:
        print(f'Password is valid')


password(input())