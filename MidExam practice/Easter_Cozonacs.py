budget=float(input())
flour=float(input())

count=0
colored_egg=0

egg=flour*0.75
milk=flour*1.25/4

price=flour+egg+milk

while budget>price:
    count+=1
    budget-=price
    colored_egg+=3
    if count%3==0:
        colored_egg-=count-2

print(f'You made {count} cozonacs! Now you have {colored_egg} eggs and {budget:.2f}BGN left.')