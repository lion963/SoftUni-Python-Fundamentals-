line=input()

total_without=0

while not line=='regular' and not line=='special':
    price=float(line)
    if price>0:
        total_without += price
    else:
        print(f'Invalid price!')

    line=input()

taxes=0.2*total_without
total_price=total_without+taxes

if line=='special':
    total_price-=0.1*total_price

if total_price>0:
    print(f"Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_without:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')
    print(f'Total price: {total_price:.2f}$')
else:
    print(f'Invalid order!')