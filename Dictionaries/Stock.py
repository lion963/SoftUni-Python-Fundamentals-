elements = input().split()
products = input().split()

stock = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    stock[key] = int(value)

for el in products:
    if el in stock.keys():
        print(f'We have {stock[el]} of {el} left')
    else:
        print(f"Sorry, we don't have {el}")
