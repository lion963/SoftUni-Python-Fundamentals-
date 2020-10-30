people_queue = int(input())
lift = list(map(int, input().split()))

capacity_wagon = 4
available_spots = (len(lift) * capacity_wagon) - sum(lift)

if available_spots == people_queue:
    lift = [capacity_wagon for el in lift]
    print(' '.join(map(str, lift)))
elif available_spots < people_queue:
    print(f"There isn't enough space! {people_queue - available_spots} people in a queue!")
    lift = [capacity_wagon for el in lift]
    print(' '.join(map(str, lift)))
elif available_spots > people_queue:
    for i in range(len(lift)):
        if lift[i]==capacity_wagon:
            pass
        elif lift[i]<capacity_wagon:
            if people_queue>capacity_wagon-lift[i]:
                people_queue-=capacity_wagon-lift[i]
                lift[i]=capacity_wagon
            else:
                lift[i]+=people_queue
                break

    print(f'The lift has empty spots!')
    print(' '.join(map(str, lift)))

# people_waiting = int(input())
# lift_state = list(map(int, input().split()))
# wagons = []
#
# for lift in lift_state:
#     while lift < 4 and people_waiting != 0:
#         lift += 1
#         people_waiting -= 1
#     wagons.append(lift)
#
# wagons_to_str = [str(wagon) for wagon in wagons]
#
# if len(wagons) * 4 == sum(wagons) and people_waiting == 0:
#     print(f"{' '.join(wagons_to_str)}")
# elif len(wagons) * 4 > sum(wagons) and people_waiting == 0:
#     print("The lift has empty spots!\n"
#           f"{' '.join(wagons_to_str)}")
# else:
#     print(f"There isn't enough space! {people_waiting} people in a queue!\n"
#           f"{' '.join(wagons_to_str)}")