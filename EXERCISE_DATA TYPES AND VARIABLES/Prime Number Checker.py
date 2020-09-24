num = input()
num = int(num)

cond = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print('False')
            cond = False
            break
if cond:
    print('True')
