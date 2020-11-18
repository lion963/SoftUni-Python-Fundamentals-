str1, str2 = input().split(' ')

sum = 0
if len(str1) == len(str2):
    for i in range(len(str1)):
        sum += ord(str1[i]) * ord(str2[i])
elif len(str1) < len(str2):
    for i in range(len(str1)):
        sum += ord(str1[i]) * ord(str2[i])
    for i in range(len(str1), len(str2)):
        sum += ord(str2[i])
elif len(str1) > len(str2):
    for i in range(len(str2)):
        sum += ord(str2[i]) * ord(str1[i])
    for i in range(len(str2), len(str1)):
        sum += ord(str1[i])

print(sum)
