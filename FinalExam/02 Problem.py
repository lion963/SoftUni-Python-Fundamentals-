import re

n = int(input())
for _ in range(n):
    password = input()
    pattern = r'(?P<start>[\W\w]+)[>]{1}([1-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([\W\w]{3})[<]{1}(?P=start)'
    result = re.findall(pattern, password)
    if result:
        password = result[0][1] + result[0][2] + result[0][3] + result[0][4]
        print(f'Password: {password}')
    else:
        print(f'Try another password!')
