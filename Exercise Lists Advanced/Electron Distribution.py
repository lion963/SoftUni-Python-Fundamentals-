electrons = int(input())

shells = []
shell_number = 1

while electrons > 0:
    add_electrons = (2 * (shell_number ** 2))
    if electrons>add_electrons:
        shells.append(add_electrons)
    else:
        shells.append(electrons)
        break
    electrons -= add_electrons
    shell_number+=1
print(shells)