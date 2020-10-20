time_per_step = list(map(int, input().split()))

slice = int((len(time_per_step) - 1) / 2)

left = time_per_step[:slice]
right = time_per_step[slice + 1:][::-1]

sum_left=0
sum_right=0
for el in left:
    if el==0:
        sum_left=sum_left*0.8
    else:
        sum_left+=el

for el in right:
    if el==0:
        sum_right = sum_right * 0.8
    else:
        sum_right += el

if sum_left<=sum_right:
    print(f'The winner is left with total time: {sum_left:.1f}')
else:
    print(f'The winner is right with total time: {sum_right:.1f}')