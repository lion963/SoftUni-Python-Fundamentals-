n = int(input())

plants_dict = {}

for _ in range(n):
    name, rarity = input().split('<->')
    rarity = int(rarity)
    if name not in plants_dict:
        plants_dict[name] = {'rarity': rarity, 'rating': []}
    else:
        plants_dict[name]['rarity'] = rarity

line = input()
while not line == 'Exhibition':
    command, action = line.split(': ')

    if command == 'Rate':
        name, rating = action.split(' - ')
        rating = int(rating)
        plants_dict[name]['rating'].append(rating)
    elif command == 'Update':
        name, new_rarity = action.split(' - ')
        new_rarity = int(new_rarity)
        plants_dict[name]['rarity'] = new_rarity
    elif command == 'Reset':
        name = action
        plants_dict[name]['rating'] = []
    else:
        print('error')

    line = input()

for plant, value in plants_dict.items():
    if value['rating']:
        value['rating'] = sum(value['rating']) / len(value['rating'])
    else:
        value['rating'] = 0.0

plants_dict = dict(sorted(plants_dict.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rating'])))

print(f'Plants for the exhibition:')
for plant, value in plants_dict.items():
    rarity = value['rarity']
    rating = value['rating']
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")
