import re

text = input()

regex = '\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4}\\b'

result = re.findall(regex, text)

print(', '.join(result))
