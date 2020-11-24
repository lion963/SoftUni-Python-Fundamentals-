import re

pattern = '[a-zA-Z0-9][\w.-]*[^_\W][@][a-zA-Z0-9][\w.-]*[a-zA-Z][.][a-zA-Z]*[^.]'

text = input()
result = re.findall(pattern, text)
print('\n'.join(result))
