""" Count Inversions of size three in a given array

https://www.geeksforgeeks.org/count-inversions-of-size-three-in-a-give-array/
"""

from collections import defaultdict


def inversionThree(nums):
    big2small = defaultdict(set)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                big2small[i].add(j)
    # DFS twice
    count = 0
    for i in range(len(nums)-2):
        for j in big2small[i]:
            for k in big2small[j]:
                count += 1
    return count


if __name__ == '__main__':
    input = [9, 6, 4, 5, 8]
    print(inversionThree(input))
