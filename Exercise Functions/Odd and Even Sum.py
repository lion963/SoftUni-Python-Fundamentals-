def even_and_odd(string):
    sum_even = 0
    sum_odd = 0
    for el in string:
        if int(el) % 2 == 0:
            sum_even += int(el)
        else:
            sum_odd += int(el)
    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')


even_and_odd(input())