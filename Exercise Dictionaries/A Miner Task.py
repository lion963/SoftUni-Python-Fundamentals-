metals_dict = {}

resource = input()

while not resource == 'stop':
    quantity = int(input())
    if resource not in metals_dict:
        metals_dict[resource] = 0
    metals_dict[resource] += quantity
    resource = input()

for key, value in metals_dict.items():
    print(f'{key} -> {value}')
