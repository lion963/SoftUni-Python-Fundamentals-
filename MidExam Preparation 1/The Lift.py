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