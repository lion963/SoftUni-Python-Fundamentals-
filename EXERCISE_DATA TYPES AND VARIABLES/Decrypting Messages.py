key = int(input())
num_char = int(input())

message = ''

for char in range(1, num_char + 1):
    letter = input()
    message += chr(ord(letter) + key)
print(message)
