list1=input().split('|')

current_energy=100
coins=100
condit=True

for el in list1:
    command, value=el.split('-')
    value=int(value)

    if command=='rest':
        if value+current_energy<=100:
            current_energy+=value
            print(f'You gained {value} energy.')
            print(f'Current energy: {current_energy}.')
        else:
            print(f'You gained {0} energy.')
            print(f'Current energy: {current_energy}.')
    elif command=='order':
        if current_energy-30>=0:
            current_energy-=30
            coins+=value
            print(f'You earned {value} coins.')
        else:
            current_energy+=50
            print(f'You had to rest!')
            continue
    else:
        if coins-value>0:
            coins-=value
            print(f'You bought {command}.')
        else:
            condit=False
            print(f'Closed! Cannot afford {command}.')
            break

if condit:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {current_energy}')