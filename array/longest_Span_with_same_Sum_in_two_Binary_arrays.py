""" Longest Span with same Sum in two Binary arrays

# https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/
"""


def longestCommonSum(arr1, arr2):
    prefixSum1, prefixSum2 = 0, 0
    diffDict = {}
    maxLength = 0
    for i, (num1, num2) in enumerate(zip(arr1, arr2)):
        prefixSum1 += num1
        prefixSum2 += num2
        currDiff = prefixSum1 - prefixSum2
        if currDiff == 0:
            maxLength = i+1
        elif currDiff not in diffDict:
            diffDict[currDiff] = i
        else:
            maxLength = max(maxLength, i - diffDict[currDiff])
    return maxLength


# Driver program
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
print("Length of the longest common",
      " span with same", end=" ")
print("sum is", longestCommonSum(arr1, arr2))
