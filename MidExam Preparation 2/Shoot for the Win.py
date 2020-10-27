targets = list(map(int, input().split()))

command = input()

while not command == 'End':
    index = int(command)
    if 0 <= index <= len(targets) - 1:
        if not targets[index] == -1:
            value = targets[index]
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] > value and not targets[i] == -1:
                    targets[i] -= value
                elif targets[i] <= value and not targets[i] == -1:
                    targets[i] += value
    command = input()

count = [1 for el in targets if el == -1]
targets = list(map(str, targets))
print(f"Shot targets: {len(count)} -> {' '.join(targets)}")