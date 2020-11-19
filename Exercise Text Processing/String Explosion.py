sequence = input()

string = ''
flag = True
add = 0

while flag:

    condit = False
    count = 0
    for i in range(len(sequence)):
        if not sequence[i] == '>':
            string += sequence[i]
            if i == len(sequence) - 1:
                flag = False
                break
        else:
            string += sequence[i]
            index = int(sequence[i + 1]) + add
            for j in range(i + 1, i + index + 1):
                if not sequence[j] == '>':
                    count += 1
                    add = index - count
                else:
                    sequence = sequence[j:]
                    count = 0
                    condit = True
                    break
        if count > 0:
            sequence = sequence[j + 1:]
            break
        if condit:
            break
print(string)
