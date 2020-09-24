n=int(input())

value=0
quality=0
snow=0
time=0

for num in range(1,n+1):
    snowball_snow=int(input())
    snowball_time=int(input())
    snowball_quality=int(input())
    snowball_value=(snowball_snow/snowball_time)**snowball_quality
    if snowball_value>value:
        value=int(snowball_value)
        quality=snowball_quality
        snow=snowball_snow
        time=snowball_time
print(f'{snow} : {time} = {value} ({quality})')