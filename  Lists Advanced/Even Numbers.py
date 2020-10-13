string = input()
indices = []
list1 = list(map(int, string.split(', ')))

for i in range(len(list1)):
    if list1[i] % 2 == 0:
        indices.append(i)

print(indices)
