""" Find longest common sub sequence """


def longestCommonSequence(nums1, nums2):
    l1, l2 = len(nums1), len(nums2)
    if l1 == 0 or l2 == 0:
        return []

    # Init the values for cache
    cache = [[0] * l2 for _ in range(l1)]
    for i in range(l1):
        if nums1[i] == nums2[0]:
            cache[i][0] = 1
    for j in range(l2):
        if nums1[0] == nums2[j]:
            cache[0][j] = 1

    for i in range(1, l1):
        for j in range(1, l2):
            if nums1[i] != nums2[j]:
                cache[i][j] = 0
            else:
                cache[i][j] = cache[i - 1][j - 1] + 1

    maxLength = 0
    for i in range(1, l1):
        for j in range(1, l2):
            if cache[i][j] > maxLength:
                maxLength = cache[i][j]

    return maxLength

