data_courses = {}

command = input()
while not command == 'end':
    course, student = command.split(' : ')

    if course not in data_courses:
        data_courses[course] = []
    data_courses[course].append(student)

    command = input()

data_courses = dict(sorted(data_courses.items(), key=lambda x: len(x[1]), reverse=True))
for key, value in data_courses.items():
    value.sort()

for key, value in data_courses.items():
    print(f'{key}: {len(value)}')
    for el in value:
        print(f'-- {el}')
