rooms_num = int(input())

free_chairs = 0
needed_chairs=0

rooms = [input().split() for _ in range(rooms_num)]
rooms_and_chairs = [[index + 1, len(rooms[index][0]) - int(rooms[index][1])] for index in range(len(rooms))]
for index in range(len(rooms_and_chairs)):
    if rooms_and_chairs[index][1] < 0:
        needed_chairs+=rooms_and_chairs[index][1]
        print(f'{abs(rooms_and_chairs[index][1])} more chairs needed in room {rooms_and_chairs[index][0]}')
    elif rooms_and_chairs[index][1] > 0:
        free_chairs += rooms_and_chairs[index][1]

if free_chairs>=0 and needed_chairs==0:
    print(f'Game On, {free_chairs} free chairs left')