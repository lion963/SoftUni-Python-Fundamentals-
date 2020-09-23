word = input()
revers = ''

for i in range(len(word) - 1, -1, -1):
    revers += word[i]

print(revers)

# print(word[::-1])
# print(word[::1])