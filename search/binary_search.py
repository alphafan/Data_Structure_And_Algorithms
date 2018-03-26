# A simple binary search implementation


def binarySearch(nums, target):
    if len(nums) == 0:
        return -1
    start, end = 0, len(nums)
    while start < end:
        mid = int((start+end)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid
    return -1


def binarySearchRec(nums, target, start, end):
    """ Binary Search

    result = binarySearchRec(nums, target, 0, len(nums)-1)
    """
    if start <= end:
        mid = int((start+end)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binarySearchRec(nums, target, mid+1, end)
        else:
            return binarySearchRec(nums, target, start, mid-1)
    else:
        return -1