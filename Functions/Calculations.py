def simple_calculator(operator, num1, num2):
    if operator=='multiply':
        return int(num1*num2)
    elif operator=='divide':
        return int(num1/num2)
    elif operator=='add':
        return int(num1+num2)
    elif operator=='subtract':
        return int(num1-num2)

oper=input()
num_1=float(input())
num_2=float(input())
print(simple_calculator(oper,num_1,num_2))