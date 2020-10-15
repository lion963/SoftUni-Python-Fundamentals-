neighborhood=list(map(int,input().split('@')))

position=0
count=0

command=input()
while not command=='Love!':
    word,value=command.split()
    value=int(value)

    if position+value>len(neighborhood)-1:
        position=0
        value=0

    if neighborhood[position+value]==0:
        print(f"Place {position+value} already had Valentine's day.")
    else:
        neighborhood[position+value]-=2

        if neighborhood[position+value]==0:
            print(f"Place {position+value} has Valentine's day.")

    position+=value
    command = input()

for el in neighborhood:
    if el>0:
        count+=1

print(f"Cupid's last position was {position}.")
if sum(neighborhood)==0:
    print(f'Mission was successful.')
else:
    print(f"Cupid has failed {count} places.")