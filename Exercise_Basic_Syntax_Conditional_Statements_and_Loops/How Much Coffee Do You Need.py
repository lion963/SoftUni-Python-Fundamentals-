line=input()

coffee=0

while line!='END':
    if line=='CODING':
        coffee+=2
    if line=='coding':
        coffee+=1
    if line=='MOVIE':
        coffee+=2
    if line=='movie':
        coffee+=1
    if line=='DOG':
        coffee+=2
    if line=='dog':
        coffee+=1
    if line=='CAT':
        coffee+=2
    if line=='cat':
        coffee+=1
    line=input()
if coffee>5:
    print('You need extra sleep')
else:
    print(coffee)