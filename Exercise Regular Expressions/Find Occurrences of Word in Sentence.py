import re

sentence = input()
word = input()

pattern='(\W|^|(?<=\s))' + word + '((?=\s)|\W|$)'
result = re.findall(pattern, sentence, re.IGNORECASE)
print(len(result))
