import re

string = input()
pattren = r'(?<=(?P<sep>\@|\#))(?P<pair_words>[A-Za-z]{3,}(?P=sep){2}[A-Za-z]{3,})(?=(?P=sep))'
pair_words = []
mirror_words = []

result = re.finditer(pattren, string)

if result:
    for el in result:
        pair_words.append(el.groupdict()['pair_words'])

if pair_words:
    print(f'{len(pair_words)} word pairs found!')
    for el in pair_words:
        if '@' in el:
            word, mirror = el.split('@@')
            if word[::-1] == mirror:
                mirror_words.append(el)
        elif '#' in el:
            word, mirror = el.split('##')
            if word[::-1] == mirror:
                mirror_words.append(el)
else:
    print(f'No word pairs found!')

if mirror_words:
    for i in range(len(mirror_words)):
        if '@' in mirror_words[i]:
            mirror_words[i] = mirror_words[i].replace('@@', ' <=> ')
        elif '#' in mirror_words[i]:
            mirror_words[i] = mirror_words[i].replace('##', ' <=> ')
    print(f'The mirror words are:')
    print(', '.join(mirror_words))
else:
    print(f'No mirror words!')
