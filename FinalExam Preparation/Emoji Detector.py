import re

text = input()
emoji_dict = {}
coolness = 1

pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})(\1)'
result = re.finditer(pattern, text)
for el in result:
    emoji_dict[el.group()] = 0

for char in text:
    if char.isdigit():
        coolness *= int(char)

for key, value in emoji_dict.items():
    sum1 = 0
    for char in key:
        sum1 += ord(char)
    emoji_dict[key] = sum1

print(f'Cool threshold: {coolness}')
print(f'{len(emoji_dict)} emojis found in the text. The cool ones are:')
for key, value in emoji_dict.items():
    if value >= coolness:
        print(key)
