target_list = input().split()

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
alphabet = alphabet.split()

sum = 0
for el in target_list:
    number = ''
    for symbol in el:
        if symbol.isdigit():
            number += symbol
    number = int(number)

    if el[0].isupper():
        number /= alphabet.index(el[0].lower()) + 1
    elif el[0].islower():
        number *= alphabet.index(el[0]) + 1

    if el[-1].isupper():
        number -= alphabet.index(el[-1].lower()) + 1
    elif el[-1].islower():
        number += alphabet.index(el[-1]) + 1

    sum += number
print(f'{sum:.2f}')
