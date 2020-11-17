line = input()
while not line == 'end':
    text = line
    rev_text = line[::-1]
    print(f'{text} = {rev_text}')
    line = input()

# line=input()
# while not line=='end':
#     text=line
#     rev_text=''
#     for ch in reversed(text):
#         rev_text+=ch
#     print(f'"{text} = {rev_text}')
#     line=input()
