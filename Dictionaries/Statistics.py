stock = {}

command = input()
while not command == "statistics":
    key, value = command.split(': ')
    value = int(value)
    if key in stock.keys():
        stock[key] += value
    else:
        stock[key] = value
    command = input()

print(f'Products in stock:')
for (key, value) in stock.items():
    print(f'- {key}: {value}')

print(f'Total Products: {len(stock.keys())}')
print(f'Total Quantity: {sum(stock.values())}')
