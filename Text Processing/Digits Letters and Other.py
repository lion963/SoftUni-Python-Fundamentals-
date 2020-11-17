text = input()

digits = ''
letters = ''
other = ''

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    elif not ch.isalpha() and not ch.isdigit():
        other += ch

print(digits)
print(letters)
print(other)
