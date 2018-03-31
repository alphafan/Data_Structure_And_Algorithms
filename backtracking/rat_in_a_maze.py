"""
    {1, 0, 0, 0}
    {1, 1, 0, 1}
    {0, 1, 0, 0}
    {1, 1, 1, 1}
"""


def ratInMaze(maze):
    """ Find path from top left to bottom right """
    if len(maze) == 0 or len(maze[0]) == 0:
        return []
    ratInMazeHelper(maze, 0, 0, len(maze), len(maze[0]), [])


def ratInMazeHelper(maze, currRow, currCol, nRow, nCol, path):
    if currRow == nRow - 1 and currCol == nCol - 1:
        print(path + [[currRow, currCol]])
        return
    if currRow + 1 < nRow and maze[currRow + 1][currCol] != 0:
        ratInMazeHelper(maze, currRow + 1, currCol,
                        nRow, nCol, path + [[currRow, currCol]])
    if currCol + 1 < nCol and maze[currRow][currCol + 1] != 0:
        ratInMazeHelper(maze, currRow, currCol + 1,
                        nRow, nCol, path + [[currRow, currCol]])


maze = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]

ratInMaze(maze)