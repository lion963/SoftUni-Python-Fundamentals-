list_message=input().split()

nested_list_message=[list(el) for el in list_message]

list_digit=[[index,nested_list_message[index][i]] for index in range(len(nested_list_message)) for i in range(len(nested_list_message[index])) if nested_list_message[index][i].isdigit()]

list_letter=[[index,nested_list_message[index][i]] for index in range(len(nested_list_message)) for i in range(len(nested_list_message[index])) if nested_list_message[index][i].isalpha()]

list_digit_w=[]
for i in range(len(list_message)):
    digit=[el[1] for el in list_digit if el[0]==i]
    list_digit_w.append(digit)

list_letter_w=[]
for i in range(len(list_message)):
    letter=[el[1] for el in list_letter if el[0]==i]
    list_letter_w.append(letter)

for el in list_letter_w:
    el[0], el[-1]=el[-1], el[0]

join_digit=[''.join(el) for el in list_digit_w]

join_letter=[''.join(el) for el in list_letter_w]

decipher_digit=[chr(int(el)) for el in join_digit]

decipher=[decipher_digit[i]+join_letter[i] for i in range(len(decipher_digit))]
decipher=' '.join(decipher)
print(decipher)