import re

race_dict = {}
names = input().split(', ')
for name in names:
    race_dict[name] = 0

line = input()
while not line == 'end of race':
    sum_digit = 0
    for symbol in line:
        if symbol.isdigit():
            sum_digit += int(symbol)
    for name in names:
        if re.search(r'[A-Z]', line).group() in name:
            race_dict[name] += sum_digit
    line = input()

race_dict = dict(sorted(race_dict.items(), key=lambda x: -x[1]))
race_123 = list(race_dict.items())[:3]
print(f'1st place: {race_123[0][0]}')
print(f'2nd place: {race_123[1][0]}')
print(f'3rd place: {race_123[2][0]}')
