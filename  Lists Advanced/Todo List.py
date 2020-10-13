command = ''
list1=[]
for i in range(11):
    list1.append(0)
while command != 'End':
    command = input()
    if not command == 'End':
        importance, todo = command.split('-')
        importance = int(importance)
        list1.pop(importance)
        list1.insert(importance, todo)

todo_list=[]
for i in range(len(list1)):
    if not list1[i]==0:
        todo_list.append(list1[i])

print(todo_list)