""" Check if two arrays are the same or not """

from collections import Counter


def isSameArray(nums1, nums2):
    if Counter(nums1) == Counter(nums2):
        return True
    return False


nums1 = [1, 1, 3, 4]
nums2 = [4, 3, 1, 1]
print(isSameArray(nums1, nums2))
