def add1(dict1, piece1, composer1, key1):
    if piece1 not in dict1:
        print(f'{piece1} by {composer1} in {key1} added to the collection!')
        dict1[piece1] = composer1
    else:
        print(f'{piece1} is already in the collection!')
    return dict1


def add2(dict2, piece1, composer1, key1):
    if piece1 not in dict2:
        dict2[piece1] = key1
    return dict2


def remove1(dict1, piece1):
    if piece1 not in dict1:
        print(f'Invalid operation! {piece1} does not exist in the collection.')
    else:
        dict1.pop(piece1)
        print(f'Successfully removed {piece1}!')
    return dict1


def remove2(dict2, piece1):
    if piece1 in dict2:
        dict2.pop(piece1)
    return dict2


def change(dict1, piece1, key1):
    if piece1 not in dict1:
        print(f'Invalid operation! {piece1} does not exist in the collection.')
    else:
        dict1[piece1] = key1
        print(f'Changed the key of {piece1} to {key1}!')
    return dict1


n = int(input())

piece_composer = {}
piece_key = {}

for i in range(n):
    piece, composer, key = input().split('|')
    piece_composer[piece] = composer
    piece_key[piece] = key

command = input()
while not command == 'Stop':
    if 'Add' in command:
        word, piece, composer, key = command.split('|')
        piece_composer = add1(piece_composer, piece, composer, key)
        piece_key = add2(piece_key, piece, composer, key)

    elif 'Remove' in command:
        word, piece = command.split('|')
        piece_composer = remove1(piece_composer, piece)
        piece_key = remove2(piece_key, piece)

    elif 'ChangeKey' in command:
        word, piece, key = command.split('|')
        piece_key = change(piece_key, piece, key)

    command = input()

piece_composer = dict(sorted(piece_composer.items(), key=lambda x: (x[0], x[1])))

for piece, composer in piece_composer.items():
    print(f'{piece} -> Composer: {composer}, Key: {piece_key[piece]}')
