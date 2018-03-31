""" Eight-Queen Problem:

https://en.wikipedia.org/wiki/Eight_queens_puzzle

"""


class EightQueens(object):

    def __init__(self):
        self.colForRow = [None] * 8
        self.numSolutions = 0

    def solvePuzzle(self):
        self.placeQueen(0)

    def placeQueen(self, row):
        if row == 8:
            self.printBoard()
            return
        for i in range(8):
            self.colForRow[row] = i
            if self.checkValid(row):
                self.placeQueen(row+1)

    def checkValid(self, row):
        for i in range(row):
            diff = self.colForRow[row] - self.colForRow[i]
            if diff == 0 or abs(diff) == row-i:
                return False
        return True

    def printBoard(self):
        board = ''
        for row, queenCol in enumerate(self.colForRow):
            rowStr = '. ' * queenCol + 'Q' + ' .' * (7-queenCol)
            board += rowStr + '\n'
        print(board)


solver = EightQueens()
solver.solvePuzzle()
