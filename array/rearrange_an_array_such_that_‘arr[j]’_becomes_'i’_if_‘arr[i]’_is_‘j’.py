""" Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’

https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/

Given an array of size n where all elements are distinct and in range from 0 to n-1, change contents of arr[]
so that arr[i] = j is changed to arr[j] = i.

Examples:

Example 1:
Input: arr[]  = {1, 3, 0, 2};
Output: arr[] = {2, 0, 3, 1};
Explanation for the above output.
Since arr[0] is 1, arr[1] is changed to 0
Since arr[1] is 3, arr[3] is changed to 1
Since arr[2] is 0, arr[0] is changed to 2
Since arr[3] is 2, arr[2] is changed to 3

Example 2:
Input: arr[]  = {2, 0, 1, 4, 5, 3};
Output: arr[] = {1, 2, 0, 5, 3, 4};

Example 3:
Input: arr[]  = {0, 1, 2, 3};
Output: arr[] = {0, 1, 2, 3};

Example 4:
Input: arr[]  = {3, 2, 1, 0};
Output: arr[] = {3, 2, 1, 0};
"""


def rearrange(input):
    for i in range(len(input)):
        input[i] += 1

    for i in range(len(input)):
        if input[i] > 0:
            rearrangeUtil(input, i)

    for i in range(len(input)):
        input[i] = -input[i] - 1
    return input


def rearrangeUtil(nums, start):
    i = start + 1
    v = nums[start]
    while v > 0:
        t = nums[v-1]
        nums[v-1] = -i
        i = v
        v = t


def rearrangeArray(nums):
    result = [None] * len(nums)
    for i, num in enumerate(nums):
        result[num] = i
    return result


test = [2, 0, 1, 4, 5, 3]
print(test)
print(rearrangeArray(test))
print(rearrange(test))
