import re

line = input()

pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'

result = re.findall(pattern, line)

print(' '.join(result))
