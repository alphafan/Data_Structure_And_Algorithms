""" Min Matrix Mutltiplication """

import sys


def minMul(matrices):
    if len(matrices) <= 2:
        return 0
    if len(matrices) == 3:
        return matrices[0] * matrices[1] * matrices[2]
    minCal = sys.maxsize
    for i in range(1, len(matrices) - 1):
        cal = minMul(matrices[:i + 1]) + \
              matrices[0] * matrices[i] * matrices[-1] + \
              minMul(matrices[i:])
        minCal = min(minCal, cal)
    return minCal


memo = {}


def minMulHelper(matrices, start, end):
    global memo
    if (start, end) in memo:
        return memo[(start, end)]
    print(start, end)
    if end - start <= 2:
        memo[(start, end)] = 0
        return 0
    if end - start == 3:
        res = matrices[start] * matrices[start + 1] * matrices[start + 2]
        memo[(start, end)] = res
    minCal = sys.maxsize
    for i in range(start + 1, end - 1):
        cal = minMulHelper(matrices, start, i + 1) + \
              matrices[start] * matrices[i] * matrices[end - 1] + \
              minMulHelper(matrices, i, end)
        minCal = min(minCal, cal)
    memo[(start, end)] = minCal
    return minCal


test = [40, 20, 30, 10, 30]
print(minMulHelper(test, 0, len(test)))
