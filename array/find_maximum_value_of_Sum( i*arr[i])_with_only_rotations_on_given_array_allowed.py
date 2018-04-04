""" Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/

Given an array, only rotation operation is allowed on array. We can rotate the array
as many times as we want. Return the maximum possible of summation of i*arr[i].

Example:

Input: arr[] = {1, 20, 2, 10}
Output: 72
We can 72 by rotating array twice.
{2, 10, 1, 20}
20*3 + 1*2 + 10*1 + 2*0 = 72

Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9};
Output: 330
We can 330 by rotating array 9 times.
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
0*1 + 1*2 + 2*3 ... 9*10 = 330

"""


def maxRotateSum(arr):
    # stores sum of arr[i]
    arrSum = 0

    # stores sum of i*arr[i]
    currVal = 0

    n = len(arr)

    for i in range(0, n):
        arrSum = arrSum + arr[i]
        currVal = currVal + (i * arr[i])

    # initialize result
    maxVal = currVal

    # try all rotations one by one and find the maximum
    # rotation sum
    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j]
        if currVal > maxVal:
            maxVal = currVal

    # return result
    return maxVal


test = [1, 20, 2, 10]
print(test)
print(maxRotateSum(test))

