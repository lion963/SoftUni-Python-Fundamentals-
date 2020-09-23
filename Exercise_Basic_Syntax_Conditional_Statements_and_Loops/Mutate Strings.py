text_1 = input()
text_2 = input()
lenght = len(text_2)
lenght_1 = len(text_1)
result = ""
result_1 = ""
for i in range(0, lenght):
    result_1 += text_2[i]
    result = ""
    for n in range(0, lenght_1):
        if n <= i:
            continue
        result += text_1[n]
    if not text_1[i] == text_2[i]:
        print(result_1 + result)