import re
from operator import itemgetter

web_list = []
pattern = r'([w]{3}.[A-Za-z0-9-]+(\.[a-z]+)+)'
while True:
    line = input()
    if line:
        web = re.findall(pattern, line)
        if web:
            web_list.append(list(map(itemgetter(0), web))[0])
    else:
        break

for el in web_list:
    print(el)
