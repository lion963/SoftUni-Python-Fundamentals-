list1=[]

while len(list1)<8:
    list1.append(int(input()))

import math
line1=math.sqrt(((list1[0]-list1[2])**2) + ((list1[1]-list1[3])**2))
line2=math.sqrt(((list1[4]-list1[6])**2) + ((list1[5]-list1[7])**2))

if line1>line2:
    if (abs(list1[0]) + abs(list1[1]))<(abs(list1[2]) + abs(list1[3])):
        print(f'({list1[0]}, {list1[1]})({list1[2]}, {list1[3]})')
    else:
        print(f'({list1[2]}, {list1[3]})({list1[0]}, {list1[1]})')
elif line1<line2:
    if (abs(list1[4]) + abs(list1[5])) < (abs(list1[6]) + abs(list1[7])):
        print(f'({list1[4]}, {list1[5]})({list1[6]}, {list1[7]})')
    else:
        print(f'({list1[6]}, {list1[7]})({list1[4]}, {list1[5]})')
elif line1==line2:
    if (abs(list1[0]) + abs(list1[1])) < (abs(list1[2]) + abs(list1[3])):
        print(f'({list1[0]}, {list1[1]})({list1[2]}, {list1[3]})')
    else:
        print(f'({list1[2]}, {list1[3]})({list1[0]}, {list1[1]})')
