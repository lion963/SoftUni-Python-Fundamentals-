archery_field = list(map(int, input().split('|')))

points = 0
command = input()

while command != 'Game over':

    if command.find('Left') >= 0:
        word, index, length = command.split('@')
        index = int(index)
        length = int(length)
        if index>len(archery_field)-1:
            pass
        else:
            shoot_index = index - length
            if shoot_index < -len(archery_field):
                shoot_index = shoot_index % len(archery_field)
                if archery_field[shoot_index]<5:
                    points+=archery_field[shoot_index]
                    archery_field[shoot_index] = 0
                else:
                    archery_field[shoot_index] -= 5
                    points += 5
            elif archery_field[shoot_index] < 5:
                points += archery_field[shoot_index]
                archery_field[shoot_index] = 0
            else:
                archery_field[shoot_index] -= 5
                points += 5

    if command.find('Right') >= 0:
        word, index, length = command.split('@')
        index = int(index)
        length = int(length)
        if index>len(archery_field)-1:
            pass
        else:
            shoot_index = index + length
            if shoot_index > len(archery_field):
                shoot_index = shoot_index % len(archery_field)
                if archery_field[shoot_index] < 5:
                    points += archery_field[shoot_index]
                    archery_field[shoot_index] = 0
                else:
                    archery_field[shoot_index] -= 5
                    points += 5
            elif archery_field[shoot_index] < 5:
                points += archery_field[shoot_index]
                archery_field[shoot_index] = 0
            else:
                archery_field[shoot_index] -= 5
                points += 5

    if command=='Reverse':
        archery_field=archery_field[::-1]

    command=input()

archery_field=list(map(str,archery_field))
print(' - '.join(archery_field))
print(f'Iskren finished the archery tournament with {points} points!')