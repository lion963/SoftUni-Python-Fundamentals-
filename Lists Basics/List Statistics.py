n=int(input())

positives=[]
negatives=[]

for i in range(1,n+1):
    line=int(input())
    if line>=0:
        positives.append(line)
    else:
        negatives.append(line)
print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')