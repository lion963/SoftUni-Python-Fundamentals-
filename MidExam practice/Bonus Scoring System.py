students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for i in range(students):
    attendance = int(input())
    bonus = (attendance / lectures) * (5 + additional_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        max_attendance = attendance

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {max_attendance} lectures.')

# students = int(input())
# lectures = int(input())
# additional_bonus = int(input())
#
# attendances = [int(input()) for i in range(students)]
#
# total_bonus = [attendance / lectures * (5 + additional_bonus) for attendance in attendances]
#
# print(f'Max Bonus: {round(max(total_bonus))}.')
# print(f'The student has attended {max(attendances)} lectures.')