# The Knight’s tour problem
"""
0  13 18 7  24
5  8  1  12 17
14 19 6  23 2
9  4  21 16 11
20 15 10 3  22
"""


tour = [[-1 for _ in range(5)] for _ in range(5)]


def knightTour():
    global tour
    tour[0][0] = 0
    place(0, 0, 0)


def place(row, col, step):
    global tour
    if step == 24:
        printTour()
        return
    for nextRow, nextCol in nextPositions(row, col):
        tour[nextRow][nextCol] = step+1
        place(nextRow, nextCol, step+1)
        tour[nextRow][nextCol] = -1


def nextPositions(row, col):
    global tour, memo
    jumpPositions = [
        [row-2, col-1], [row-2, col+1],
        [row-1, col-2], [row-1, col+2],
        [row+2, col-1], [row+2, col+1],
        [row+1, col-2], [row+1, col+2]
    ]
    nextPositions = []
    for nextRow, nextCol in jumpPositions:
        if 0 <= nextRow < 5 and \
           0 <= nextCol < 5 and \
           tour[nextRow][nextCol] == -1:
            nextPositions.append([nextRow, nextCol])
    return nextPositions


def printTour():
    global tour
    for row in tour:
        rowString = ''
        for num in row:
            rowString += str(num) + ' '
        print(rowString)
    print()


knightTour()
