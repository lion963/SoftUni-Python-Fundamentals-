string_list=input().split()
result=''
for string in string_list:
    n=len(string)
    result+=string*n
print(result)