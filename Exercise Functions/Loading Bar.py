def loading(percent):
    level = int(percent / 10) * '%'
    point = (10 - int(percent / 10)) * '.'
    if percent <= 90:
        print(str(percent)+'% '+'[' + level + point + ']')
        print('Still loading...')
    else:
        print('100% Complete!')
        print('[' + level + point + ']')


loading(int(input()))