str_happiness = input()
increase_happiness = int(input())
count = 0

happiness = list(map(lambda x: int(x) * increase_happiness, str_happiness.split()))
average = sum(happiness) / len(happiness)
for el in happiness:
    if el >= average:
        count += 1

if count >= len(happiness)/2:
    print(f'Score: {count}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {count}/{len(happiness)}. Employees are not happy!')