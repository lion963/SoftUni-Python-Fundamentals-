items_dict = {}
condit = True

while condit:
    list1 = input().split()

    for i in range(0, len(list1), 2):
        quantity = int(list1[i])
        key = list1[i + 1].lower()
        if key not in items_dict:
            items_dict[key] = 0
        items_dict[key] += quantity

        if 'shards' in items_dict:
            if items_dict['shards'] >= 250:
                items_dict['shards'] -= 250
                print(f'Shadowmourne obtained!')
                condit = False
                break
        if 'fragments' in items_dict:
            if items_dict['fragments'] >= 250:
                items_dict['fragments'] -= 250
                print(f'Valanyr obtained!')
                condit = False
                break
        if 'motes' in items_dict:
            if items_dict['motes'] >= 250:
                items_dict['motes'] -= 250
                print(f'Dragonwrath obtained!')
                condit = False
                break
    list1 = []

searched_items_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
for key, value in items_dict.items():
    if key == 'shards' or key == 'fragments' or key == 'motes':
        searched_items_dict[key] += value
searched_items_dict = dict(sorted(searched_items_dict.items()))
searched_items_dict = dict(sorted(searched_items_dict.items(), key=lambda x: x[1], reverse=True))
for key, value in searched_items_dict.items():
    print(f'{key}: {value}')

the_rest_dict = {key: value for key, value in items_dict.items() if
                 key != 'shards' and key != 'fragments' and key != 'motes'}
the_rest_dict = dict(sorted(the_rest_dict.items(), key=lambda x: x[0]))
for key, value in the_rest_dict.items():
    print(f'{key}: {value}')
