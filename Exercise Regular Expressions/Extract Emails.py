import re

text = input()
pattern = r"(?<=^|(?<=\s))([A-Za-z0-9][\w.-]+?[A-Za-z0-9]@[A-Za-z][A-Za-z.-]+?[A-Za-z].[A-Za-z]+)(?=.$|(?=\s))"
result = re.findall(pattern, text)
print('\n'.join(result))
