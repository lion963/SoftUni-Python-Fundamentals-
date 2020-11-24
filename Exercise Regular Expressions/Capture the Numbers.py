import re

result = []
string = []

while True:
    line = input()
    if line:
        string.append(line)
    else:
        break

pattern = '[0-9]+'

for el in string:
    result += re.findall(pattern, el)

print(' '.join(result))
