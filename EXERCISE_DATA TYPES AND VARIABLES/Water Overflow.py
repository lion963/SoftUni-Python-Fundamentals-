n = int(input())

capacity = 255
water = 0

for i in range(1, n + 1):
    line = int(input())
    water += line
    if water > capacity:
        print(f'Insufficient capacity!')
        water -= line
print(water)
