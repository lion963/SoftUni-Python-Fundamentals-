list1=[int(input()),int(input())]
list2=[int(input()),int(input())]

import math
list_point1=list(map(lambda x: abs(x**2),list1))
distance1=math.sqrt(sum(list_point1))
list_point2=list(map(lambda x: abs(x**2),list2))
distance2=math.sqrt(sum(list_point2))


if distance1>distance2:
    print(f'({list2[0]}, {list2[1]})')
elif distance1<distance2:
    print(f'({list1[0]}, {list1[1]})')
elif distance1==distance2:
    print(f'({list1[0]}, {list1[1]})')