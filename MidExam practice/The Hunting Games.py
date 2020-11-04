days = int(input())
people = int(input())
energy = float(input())
water = float(input())
food = float(input())

total_water = people * days * water
total_food = people * days * food

for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        break
    if day % 2 == 0:
        energy += energy * 0.05
        total_water -= total_water * 0.30
    if day % 3 == 0:
        energy += energy * 0.10
        total_food -= total_food / people

if energy > 0:
    print(f'You are ready for the quest. You will be left with - {energy:.2f} energy!')
else:
    print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
