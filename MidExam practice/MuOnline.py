dungeons_rooms = input().split('|')
dungeons_rooms = [list(el.split()) for el in dungeons_rooms]

health = 100
bitcoins = 0

for i in range(len(dungeons_rooms)):
    if dungeons_rooms[i][0] == 'potion':
        best_room = i
        if health + int(dungeons_rooms[i][1]) > 100:
            print(f'You healed for {100 - health} hp.')
            health = 100
            print(f'Current health: {health} hp.')
        else:
            print(f'You healed for {dungeons_rooms[i][1]} hp.')
            health += int(dungeons_rooms[i][1])
            print(f'Current health: {health} hp.')
    elif dungeons_rooms[i][0] == 'chest':
        best_room = i
        print(f'You found {dungeons_rooms[i][1]} bitcoins.')
        bitcoins += int(dungeons_rooms[i][1])
    else:
        best_room = i
        health -= int(dungeons_rooms[i][1])
        if health > 0:
            print(f'You slayed {dungeons_rooms[i][0]}.')
        else:
            print(f'You died! Killed by {dungeons_rooms[i][0]}.')
            print(f'Best room: {best_room + 1}')
            break

if health > 0:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')