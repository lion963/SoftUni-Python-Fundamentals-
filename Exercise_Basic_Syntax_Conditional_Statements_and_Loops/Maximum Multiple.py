divisor = int(input())
bound = int(input())

import sys

max = -sys.maxsize

for i in range(1, bound + 1):
    if i % divisor == 0 and 0 <= i <= bound:
        max = i
print(max)
