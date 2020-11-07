pirate_ship = list(map(int, input().split('>')))
war_ship = list(map(int, input().split('>')))
health = int(input())

needed_repair_value = health * 0.20
condit = False
command = input()

while not command == 'Retire':
    command_list = command.split()
    if command.find('Fire') >= 0:
        index1 = int(command_list[1])
        demage = int(command_list[2])
        if index1 in range(len(war_ship)):
            war_ship[index1] -= demage
            if war_ship[index1] <= 0:
                print(f'You won! The enemy ship has sunken.')
                condit = True
                break
    elif command.find('Defend') >= 0:
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        demage = int(command_list[3])
        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= demage
                if pirate_ship[i] <= 0:
                    print(f'You lost! The pirate ship has sunken.')
                    condit = True
                    break
    elif command.find('Repair') >= 0:
        index1 = int(command_list[1])
        repair_health = int(command_list[2])
        if index1 in range(len(pirate_ship)):
            if pirate_ship[index1] + repair_health <= health:
                pirate_ship[index1] += repair_health
            else:
                pirate_ship[index1] = health
    elif command.find('Status') >= 0:
        repair_sections = [el for el in pirate_ship if el < needed_repair_value]
        print(f'{len(repair_sections)} sections need repair.')

    command = input()

if not condit:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(war_ship)}')
