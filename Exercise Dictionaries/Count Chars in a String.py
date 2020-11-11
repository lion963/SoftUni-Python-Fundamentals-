string = input()

dict_string = {}

for letter in string:
    if not letter == ' ':
        if letter not in dict_string:
            dict_string[letter] = 0
        dict_string[letter] += 1

for key, value in dict_string.items():
    print(f'{key} -> {value}')
