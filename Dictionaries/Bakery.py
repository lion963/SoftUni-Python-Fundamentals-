products = input().split()
bakery = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    bakery[key] = int(value)
print(bakery)

for key in bakery.keys():
    print(key, end=' ')
    print(bakery[key], end=' ')
    print(bakery.get(key), end=' ')
print()

for value in bakery.values():
    print(value, end=' ')
print()

for key in bakery.keys():
    bakery[key] *= 2
print(bakery)

for (key, value) in bakery.items():
    print(key, value)

if 'bread' in bakery:
    print(bakery['bread'])

if 'bread' in bakery.keys():
    print(bakery['bread'])

if 24 in bakery.values():
    print('OK')
