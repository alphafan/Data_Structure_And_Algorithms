""" Reorder an array according to given indexes

https://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/

Given two integer arrays of same size, “arr[]” and “index[]”, reorder elements in “arr[]”
according to given index array. It is not allowed to given array arr’s length.

Example:

Input:  arr[]   = [10, 11, 12];
        index[] = [1, 0, 2];
Output: arr[]   = [11, 10, 12]
        index[] = [0,  1,  2]

Input:  arr[]   = [50, 40, 70, 60, 90]
        index[] = [3,  0,  4,  1,  2]
Output: arr[]   = [40, 60, 90, 50, 70]
        index[] = [0,  1,  2,  3,   4]
Expected time complexity O(n) and auxiliary space O(1)

"""


def reorderArray(nums, order):
    for i in range(len(nums)):
        index = order.index(i)
        swap(nums, i, index)
        swap(order, i, index)
    return nums, order


def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]


arr = [50, 40, 70, 60, 90]
index = [3,  0,  4,  1,  2]
print(reorderArray(arr, index))
