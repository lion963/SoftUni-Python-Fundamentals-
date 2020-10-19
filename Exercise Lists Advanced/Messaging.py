numbers = input().split()
text = list(input())

message = ''
numbers=[list(map(int, el)) for el in numbers]
indexes = [sum(el) for el in numbers]


for num in indexes:
    if num > len(text) - 1:
        message += text[num - len(text)]
        text.pop(num - len(text))
    else:
        message += text[num]
        text.pop(num)

print(message)