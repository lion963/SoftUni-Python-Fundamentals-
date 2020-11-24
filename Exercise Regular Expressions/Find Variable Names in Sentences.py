import re

list1 = input().split()
result = []
pattern = '^[_][0-9A-Za-z]*[0-9A-Za-z]$'

for el in list1:
    result += re.findall(pattern, el)
result = [el[1:] for el in result]
print(','.join(result))
