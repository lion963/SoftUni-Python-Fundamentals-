old_version = list(map(int,input().split('.')))

if old_version[2] < 9:
    old_version.append(old_version[2] + 1)
    old_version.pop(-2)
elif old_version[2]==9:
    old_version.pop(2)
    old_version.append(0)
    if old_version[1]<9:
        old_version.insert(1, old_version[1] + 1)
        old_version.pop(2)
    elif old_version[1]==9:
        old_version.pop(1)
        old_version.insert(1,0)
        old_version.insert(0, old_version[0] + 1)
        old_version.pop(1)

new_version = '.'.join(list(map(str,old_version)))
print(new_version)