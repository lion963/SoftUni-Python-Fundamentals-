employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
total_people = int(input())

people_per_hour = employee1 + employee2 + employee3

total_hour = 0

while total_people > 0:
    total_hour += 1
    if total_hour % 4 == 0:
        pass
    else:
        total_people -= people_per_hour

print(f'Time needed: {total_hour}h.')
