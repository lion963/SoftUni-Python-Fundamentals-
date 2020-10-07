coffee_p = 1.50
water_p = 1.00
coke_p = 1.40
snacks_p = 2.00


def amount(item, quantity):
    if item == 'water':
        return quantity * water_p
    elif item == 'coffee':
        return quantity * coffee_p
    elif item == 'coke':
        return quantity * coke_p
    elif item == 'snacks':
        return quantity * snacks_p


print(f'{amount(input(), int(input())):.2f}')
