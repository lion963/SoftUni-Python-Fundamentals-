def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(total, num):
    sub1 = total - num
    print(sub1)


def add_and_subtract(a=int(input()), b=int(input()), c=int(input())):
    subtract(sum_numbers(a, b), c)


add_and_subtract()