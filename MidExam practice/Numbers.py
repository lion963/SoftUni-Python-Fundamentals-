list_numbers = list(map(int, input().split()))

average = sum(list_numbers) / len(list_numbers)

list_above_avg = [num for num in list_numbers if num > average]
list_above_avg.sort()
list_above_avg = list_above_avg[::-1]

if len(list_above_avg) >= 5:
    list_above_avg = list_above_avg[0:5]

if len(list_above_avg) == 0:
    print('No')
else:
    print(' '.join(map(str, list_above_avg)))
