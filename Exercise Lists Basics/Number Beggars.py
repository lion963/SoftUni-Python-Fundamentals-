str1 = input()
begs = int(input())

list1 = str1.split(', ')
n = begs
sum = 0
list2 = []

while n > 0:
    for i in range(begs - n, len(list1), begs):
        if i > len(list1) - 1:
            sum += 0
        else:
            sum += int(list1[i])
    list2.append(sum)
    sum = 0
    n -= 1
print(list2)
