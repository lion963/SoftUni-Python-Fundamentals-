items_dict = {}

command = input()
while not command == 'buy':
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in items_dict:
        items_dict[name] = [0, 0]
    items_dict[name][0] = price
    items_dict[name][1] += quantity

    command = input()

for key, value in items_dict.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')
