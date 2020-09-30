n=int(input())

even_nums=[]
odd_nums=[]
negative_nums=[]
positive_nums=[]

for iter in range(n):
    line=int(input())
    if line%2==0:
        even_nums.append(line)
    if not line%2==0:
        odd_nums.append(line)
    if line<0:
        negative_nums.append(line)
    if line>=0:
        positive_nums.append(line)
criteria=input()
if criteria=='positive':
    print(positive_nums)
elif criteria=='negative':
    print(negative_nums)
elif criteria=='even':
    print(even_nums)
elif criteria=='odd':
    print(odd_nums)