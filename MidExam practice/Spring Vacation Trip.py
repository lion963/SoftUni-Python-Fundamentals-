days = int(input())
budget = float(input())
people = int(input())
price_fuel_km = float(input())
food_exp_day = float(input())
room_price_day = float(input())

food_exp = days * food_exp_day * people
room_exp = days * room_price_day * people
if people > 10:
    room_exp -= room_exp * 0.25

expenses = food_exp + room_exp

count_days = 1
while count_days <= days:
    distance = float(input())

    expenses += distance * price_fuel_km

    if count_days % 3 == 0 or count_days % 5 == 0:
        expenses += expenses * 0.40
    if count_days % 7 == 0:
        expenses -= expenses / people

    if expenses > budget:
        break

    count_days += 1

if expenses > budget:
    print(f'Not enough money to continue the trip. You need {(expenses - budget):.2f}$ more.')
else:
    print(f'You have reached the destination. You have {(budget - expenses):.2f}$ budget left.')
