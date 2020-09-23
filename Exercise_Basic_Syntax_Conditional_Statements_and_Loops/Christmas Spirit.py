quantity=int(input())
days=int(input())

ornament=2
skirt=5
garlands=3
lights=15

amount=0
spirit=0
counter=0

for i in range(1,days+1):
    counter+=1
    if i%11==0:
        quantity+=2
    if i%2==0:
        amount+=quantity*ornament
        spirit+=5
    if i%3==0:
        amount+=quantity*(skirt+garlands)
        spirit+=13
    if i%5==0:
        amount+=quantity*lights
        spirit+=17
    if i%15==0:
        spirit+=30
    if i%10==0:
        amount+=(skirt+garlands+lights)
        spirit-=20
if counter%10==0:
    spirit-=30
print(f'Total cost: {amount}')
print(f'Total spirit: {spirit}')