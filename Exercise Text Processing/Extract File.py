path_list = input().split('\\')

for el in path_list:
    if '.' in el:
        file, extension = el.split('.')
        print(f'File name: {file}')
        print(f'File extension: {extension}')
