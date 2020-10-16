rows = int(input())

moves = 1
old_position = []

matrix = [list(input()) for _ in range(rows)]

while True:
    condit = False

    position = [[r, c] for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == 'k']
    position = [position[0][0], position[0][1]]

    if position[0] == 0 or position[0] == 3:
        print(f'Kate got out in {moves} moves')
        break
    elif (position[1] == 0 or position[1] == 5) and (position[0] == 1 or position[0] == 2):
        print(f'Kate got out in {moves} moves')
        break

    old_moves = moves
    for row in range(position[0] - 1, position[0] + 2):
        if condit:
            break
        for col in range(position[1] - 1, position[1] + 2):
            if matrix[row][col] == ' ':
                current = [row, col]
                if not current in old_position:
                    moves += 1
                    matrix[row][col] = 'k'
                    matrix[position[0]][position[1]] = ' '
                    condit = True
                    break
    if old_moves == moves:
        print(f'Kate cannot get out')
        break
    old_position.append(position)
