n=int(input())
word=input()
words=[]
match_words=[]

for iter in range(n):
    line=input()
    words.append(line)
    if word in line:
        match_words.append(line)
print(words)
print(match_words)