line1=input().split(' ')
line2=input().split(' ')
line3=input().split(' ')

for i in range(3):
    line1[i]=int(line1[i])
    line2[i] = int(line2[i])
    line3[i] = int(line3[i])

if line1[0]==line1[1]==line1[2]==1 or line2[0]==line2[1]==line2[2]==1 or line3[0]==line3[1]==line3[2]==1:
    print(f'First player won')
elif sum(line1)==6 or sum(line2)==6 or sum(line3)==6:
    print(f'Second player won')
elif line1[0]==line2[0]==line3[0]==1 or line1[1]==line2[1]==line3[1]==1 or line1[2]==line2[2]==line3[2]==1:
    print(f'First player won')
elif line1[0]==line2[0]==line3[0]==2 or line1[1]==line2[1]==line3[1]==2 or line1[1]==line2[1]==line3[1]==2:
    print(f'Second player won')
elif line1[0]==line2[1]==line3[2]==1 or line1[2]==line2[1]==line3[0]==1:
    print(f'First player won')
elif line1[0]==line2[1]==line3[2]==2 or line1[2]==line2[1]==line3[0]==2:
    print(f'Second player won')
else:
    print(f'Draw!')