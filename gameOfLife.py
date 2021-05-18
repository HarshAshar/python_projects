board = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]

rows = len(board)
cols = len(board[0])

def gameOfLife(board):

    # create empty list of all 0s
    newBoard = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):

            aliveNeighbours = calculateAliveNeighbours(i, j)

            print(aliveNeighbours)

            if board[i][j] == 0 and aliveNeighbours == 3:
                newBoard[i][j] = 1
            elif board[i][j] == 1 and (aliveNeighbours < 2 or aliveNeighbours > 3):
                newBoard[i][j] = 0
            elif board[i][j] == 1 and (aliveNeighbours == 2 or aliveNeighbours == 3):
                newBoard[i][j] = 1
            else:
                newBoard[i][j] = board[i][j]

    return newBoard


def calculateAliveNeighbours(row, col):

    count = 0

    for x in range(-1, 2):
        for y in range(-1, 2):

            if (row + x) < 0 or (col + y) < 0 or (row + x) == rows or (col + y) == cols:
                continue

            tempRow = (row + x + rows) % rows
            tempCol = (col + y + cols) % cols

            # print(x, y)
            # print(tempRow, tempCol)

            count += board[tempRow][tempCol]

    return count - board[row][col]




nextState = gameOfLife(board)

print(nextState)