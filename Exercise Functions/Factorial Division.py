def factorial(num1, num2):
    factorial1=1
    factorial2=1
    for i in range(1, num1 + 1):
        factorial1 *= i
    for i in range(1, num2 + 1):
        factorial2 *= i
    result = factorial1 / factorial2
    return result


print(f'{factorial(int(input()), int(input())):.2f}')