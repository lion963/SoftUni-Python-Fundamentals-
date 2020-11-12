n = int(input())

students = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

students_average = {key: (sum(value) / len(value)) for key, value in students.items() if
                    (sum(value) / len(value)) >= 4.50}
students_average = dict(sorted(students_average.items(), key=lambda x: x[1], reverse=True))

for key, value in students_average.items():
    print(f'{key} -> {value:.2f}')
