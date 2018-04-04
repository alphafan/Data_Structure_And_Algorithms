""" Min cost path """


def minCostPath(grid):
    """ Find the minimal cost path from top-left to bottom-right

    Args:
        grid: list[list]: 2-D array representing the grid

    Returns:
        path: list[[row, col]]: List of path points
            Each item is a [col, row]
    """
    cache = grid
    nRow, nCol = len(grid), len(grid[0])
    for row in range(1, nRow):
        for col in range(1, nCol):
            cache[row][col] = grid[row][col] + min(cache[row-1][col-1],
                                                   cache[row][col-1],
                                                   cache[row-1][col])
    return cache[-1][-1]
