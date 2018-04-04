""" Count the number of possible triangles

https://www.geeksforgeeks.org/find-number-of-triangles-possible/

Given an unsorted array of positive integers. Find the number of triangles that can be formed with three different array
elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any two values (or sides)
must be greater than the third value (or third side).

For example, if the input array is {4, 6, 3, 7}, the output should be 3. There are three triangles possible {3, 4, 6},
{4, 6, 7} and {3, 6, 7}. Note that {3, 4, 7} is not a possible triangle.

As another example, consider the array {10, 21, 22, 100, 101, 200, 300}. There can be 6 possible triangles: {10, 21, 22}
, {21, 100, 101}, {22, 100, 101}, {10, 100, 101}, {100, 101, 200} and {101, 200, 300}
"""

import random


def numOfTriangles(nums):
    # To form a triangle, sum_of_min_2 > largest
    # Brute force:
    #   i, j, k in array, if i + j > k, append to result --> O(n3)
    # Sorting and find values that are larger then i + k --> O(nlogn) + O(n2)
    nums, length = sorted(nums), len(nums)
    result = []
    for i in range(length):
        for j in range(i+1, length):
            startIndex = endIndex = j + 1
            # To Optimize, Use binary search
            for k in range(length-1, j, -1):
                if nums[i] + nums[j] > nums[k]:
                    endIndex = k+1
                    break
            for k in range(startIndex, endIndex):
                result.append([nums[i], nums[j], nums[k]])
    return len(result)


n = [random.randint(1, 10) for _ in range(5)]
print(n)
print(numOfTriangles(n))
