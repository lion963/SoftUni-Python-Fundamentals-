list1=[int(input()),int(input()),int(input())]

neg=0
zer=0

for el in list1:
    if el<0:
        neg+=1
    if el==0:
        zer+=1

if zer>0:
    print('zero')
elif not neg%2==0:
    print('negative')
else:
    print('positive')