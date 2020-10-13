numbers = input().split()

# numbers=sorted(numbers, reverse=True)
# numbers.reverse()
numbers.sort(reverse=True)

numbers=''.join(numbers)
print(numbers)