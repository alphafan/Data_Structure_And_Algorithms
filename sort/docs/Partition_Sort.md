# Quick Sort (Partition Sort)

```python
# A Simple Implementation of Partition Sort


def partitionSort(nums):
    partitionSortHelper(nums, 0, len(nums)-1)
    return nums


def partitionSortHelper(nums, start, end):
    if start < end:
        splitIndex = partition(nums, start, end)
        partitionSortHelper(nums, start, splitIndex-1)
        partitionSortHelper(nums, splitIndex+1, end)


def partition(nums, start, end):
    pivotIndex = int((start+end)/2)
    pivot = nums[pivotIndex]
    swap(nums, pivotIndex, end)
    splitIndex = start
    while start < end:
        if nums[start] < pivot:
            swap(nums, start, splitIndex)
            splitIndex += 1
        start += 1
    swap(nums, splitIndex, end)
    return splitIndex


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
```