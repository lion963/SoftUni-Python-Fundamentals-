def plunder(dict1, city1, people1, gold1):
    dict1[city1]['population'] -= people1
    dict1[city1]['gold'] -= gold1
    print(f'{city1} plundered! {gold1} gold stolen, {people1} citizens killed.')
    if dict1[city1]['population'] <= 0 or dict1[city1]['gold'] <= 0:
        dict1.pop(city1)
        print(f'{city1} has been wiped off the map!')
    return dict1


def prosper(dict1, city1, gold1):
    dict1[city1]['gold'] += gold1
    total_gold = dict1[city1]['gold']
    print(f'{gold1} gold added to the city treasury. {city1} now has {total_gold} gold.')
    return dict1


city_dict = {}

city_str = input()
while not city_str == 'Sail':
    city, population, gold = city_str.split('||')
    population = int(population)
    gold = int(gold)
    if city not in city_dict:
        city_dict[city] = {'population': population, 'gold': gold}
    else:
        city_dict[city]['population'] += population
        city_dict[city]['gold'] += gold
    city_str = input()

line = input()
while not line == 'End':
    command_list = line.split('=>')

    if command_list[0] == 'Plunder':
        city = command_list[1]
        people = int(command_list[2])
        gold = int(command_list[3])
        city_dict = plunder(city_dict, city, people, gold)
    elif command_list[0] == 'Prosper':
        city = command_list[1]
        gold = int(command_list[2])
        if gold > 0:
            city_dict = prosper(city_dict, city, gold)
        else:
            print(f'Gold added cannot be a negative number!')

    line = input()

if city_dict:
    city_dict = dict(sorted(city_dict.items(), key=lambda x: (-x[1]['gold'], x[0])))
    print(f'Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:')
    for city, value in city_dict.items():
        people = value['population']
        gold = value['gold']
        print(f'{city} -> Population: {people} citizens, Gold: {gold} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
