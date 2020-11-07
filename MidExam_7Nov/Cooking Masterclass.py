budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

eggs = students * price_egg * 10
import math

aprons = (students + math.ceil(students * 0.20)) * price_apron

if students // 5 > 0:
    students -= students // 5

flours = students * price_flour

expenses = eggs + aprons + flours

if expenses <= budget:
    print(f'Items purchased for {expenses:.2f}$.')
else:
    print(f'{(expenses - budget):.2f}$ more needed.')
