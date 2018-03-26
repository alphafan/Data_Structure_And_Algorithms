# Quick Sort (Merge Sort)

```python
# A simple merge sort implementation in Python


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = int(len(nums)/2)
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    i, j, res = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append((right[j]))
            j += 1
        if i == len(left):
            res.extend(right[j:])
            break
        if j == len(right):
            res.extend(left[i:])
    return res
```