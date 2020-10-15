targets=list(map(int,input().split()))
command=''

while not command=='End':
    command=input()
    if command=='End':
        break

    word, index, value = command.split()
    index=int(index)
    value=int(value)

    if word=='Shoot':
        if index>len(targets)-1:
            continue
        else:
            targets[index]-=value
            if targets[index]<=0:
                targets.pop(index)

    elif word == 'Add':
        if index > len(targets) - 1:
            print(f'Invalid placement!')
            continue
        else:
            targets.insert(index,value)

    elif word == 'Strike':
        strike_list=[]
        if value*2+1>len(targets):
            print(f'Strike missed!')
        else:
            for i in range(index-value,index+value+1):
                strike_list.append(targets[i])
        for el in strike_list:
            targets.remove(el)

targets=list(map(str,targets))
joined='|'.join(targets)
print(joined)