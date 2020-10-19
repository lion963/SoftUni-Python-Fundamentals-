list1=list(input())
result=[]
index=0

numbers=[int(el) for el in list1 if el.isdigit()]
non_numbers=[el for el in list1 if not el.isdigit()]

take=[numbers[i] for i in range(len(numbers)) if i%2==0]
skip=[numbers[i] for i in range(len(numbers)) if not i%2==0]

for i in range(len(take)):
    result+=non_numbers[index:index+take[i]]
    index += take[i]+skip[i]
result=''.join(result)
print(result)