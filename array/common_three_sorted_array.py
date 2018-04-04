""" Find common elements in three sorted array

https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/
"""


def commonElements(nums1, nums2, nums3):
    l1, l2, l3 = len(nums1), len(nums2), len(nums3)
    i, j, k = 0, 0, 0
    results = []
    while i < l1 and j < l2 and k < l3:
        if nums1[i] == nums2[j] and nums2[j] == nums3[k]:
            results.append(nums1[i])
            i += 1
            j += 1
            k += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums3[k]:
            j += 1
        else:
            k += 1
    return results


if __name__ == '__main__':
    input1 = [1, 5, 10, 20, 40, 80]
    input2 = [6, 7, 20, 80, 100]
    input3 = [3, 4, 15, 20, 30, 70, 80, 120]

    print(commonElements(input1, input2, input3))
