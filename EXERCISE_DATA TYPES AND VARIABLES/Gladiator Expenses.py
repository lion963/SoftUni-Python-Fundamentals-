lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

amount = 0

for lost in range(1, lost_fight + 1):
    if lost % 2 == 0:
        amount += helmet_price
    if lost % 3 == 0:
        amount += sword_price
    if lost % 6 == 0:
        amount += shield_price
    if lost % 12 == 0:
        amount += armor_price
print(f'Gladiator expenses: {amount:.2f} aureus')
