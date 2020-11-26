import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(?P<no>.\d+)?)!(?P<quantity>\d+)"
date = ''
sum = 0
command = input()
while not command == "Purchase":
    if re.search(pattern, command):
        date += ' ' + command
    command = input()

result = re.finditer(pattern, date)
print(f'Bought furniture:')
for el in result:
    dict1 = el.groupdict()
    print(dict1['name'])
    sum += float(dict1['price']) * int(dict1['quantity'])
print(f'Total money spend: {sum:.2f}')
