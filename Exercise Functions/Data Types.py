comand=input()
value=input()

if comand=='int':
    print(int(value)*2)
elif comand=='real':
    print(f'{(float(value)*1.5):.2f}')
elif comand=='string':
    print(f'${value}$')