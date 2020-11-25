import re

sentence = input()
word = input()

pattern='[\W]*' + word + '[\W]'
result = re.findall(pattern, sentence, re.IGNORECASE)
print(len(result))
