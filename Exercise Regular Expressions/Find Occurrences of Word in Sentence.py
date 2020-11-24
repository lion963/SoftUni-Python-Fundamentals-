import re

sentence = input()
word = input()

result = re.findall("[\W]*" + word + "[\W]", sentence, re.IGNORECASE)
print(len(result))
