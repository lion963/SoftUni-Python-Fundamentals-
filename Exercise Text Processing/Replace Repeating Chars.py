sequence = input()

uniq = ''
letter = ''
count = 0
while True:
    sequence = sequence.replace(letter, '', count)
    if sequence == '':
        break
    letter = sequence[0]
    uniq += letter
    count = 0
    for el in sequence:
        if el == letter:
            count += 1
        else:
            break
print(uniq)
