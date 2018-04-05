""" Egg Drop """

import sys


def eggDrop(nFloors, nEggs, memo):
    """ Get the minimal drops.

    Ideas:
        Drop from floor X:
        - Egg breaks, try 1, 2, ... , X-1        -> eggDrop(X-1, nEggs-1)
        - Not break, try X+1, X+2, ..., nFloors  -> eggDrop(nFloors-X, nEggs)

        Worst Case for dropping at X:
            f(X) = 1 + min(eggDrop(X-1, nEggs-1), eggDrop(nFloors-X, nEggs))
        Worst Case fro nFloors and nEggs
            max(f(X): X = 1, 2, 3, ..., nFloors)

        Base Cases:
        - nFloors == 0 --> return 0
        - nFloors != 0 nEggs == 1 --> return nFloors
    """
    if (nFloors, nEggs) in memo:
        return memo[(nFloors, nEggs)]
    if nFloors == 0 or nFloors == 1 or nEggs == 1:
        memo[(nFloors, nEggs)] = nFloors
        return nFloors
    maxDrops = sys.maxsize
    for i in range(1, nFloors + 1):
        # Egg breaks
        drops1 = eggDrop(i - 1, nEggs - 1, memo)
        # Not break
        drops2 = eggDrop(nFloors - i, nEggs, memo)
        drops = 1 + max(drops1, drops2)
        maxDrops = min(maxDrops, drops)
    memo[(nFloors, nEggs)] = maxDrops
    return maxDrops


print(eggDrop(36, 2, {}))
