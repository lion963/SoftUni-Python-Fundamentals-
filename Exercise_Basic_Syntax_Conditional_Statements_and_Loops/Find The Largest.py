str1=input()

def Convert(string):
    li=[]
    li[:0]=string
    return li

list1=Convert(str1)
list1.sort(reverse=True)

def listToString(list1):
  str = ""
  for i in list1:
    str += i
  return str

final=int(listToString(list1))
print(final)