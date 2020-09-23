line=input()

string=str(line)

for indes, digit in enumerate(string):
    print(f'{digit}{digit}', end='')