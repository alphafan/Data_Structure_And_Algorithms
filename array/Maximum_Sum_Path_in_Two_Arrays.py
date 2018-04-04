""" Maximum Sum Path in Two Arrays

Given two sorted arrays such the arrays may have some common elements.
Find the sum of the maximum sum path to reach from beginning of any array
to end of any of the two arrays. We can switch from one array to another
array only at common elements.

Expected time complexity is O(m+n) where m is the number of elements in ar1[]
and n is the number of elements in ar2[].

https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/
"""


def maxSumPath(nums1, nums2):
    result= []
    start, end = 0, 0
    len1, len2 = len(nums1), len(nums2)
    if len1 > len2:
        nums1, len1, nums2, len2 = nums2, len2, nums1, len1
    while end < len1:
        if nums1[end] == nums2[end]:
            # common element found
            # Compute the sub sum for each and choose the larger one to result
            subSum1 = sum(nums1[start:end+1])
            subSum2 = sum(nums2[start:end+1])
            if subSum1 > subSum2:
                result.extend(nums1[start:end+1])
            else:
                result.extend(nums2[start:end+1])
            start = end + 1
        end += 1
    if len(result) == len1:
        if len2 > len1 and sum(nums2[len1:len2]) > 0:
            result.extend(nums2[len1:len2])
        return result
    if sum(nums1[len(result):]) > sum(nums2[len(result):2]):
        result.extend(nums1[len(result):])
    else:
        result.extend(nums2[len(result):])
    return result


if __name__ == '__main__':
    input1 = [2, 3, 7, 10, 12, 15, 30, 34]
    input2 = [1, 5, 7, 8, 10, 15, 16, 19]

    print(maxSumPath(input1, input2))
