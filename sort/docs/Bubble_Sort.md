# Bubble Sort

```python
import random


def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                swap(nums, i, j)
    return nums


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


n = [random.randint(0, 20) for _ in range(10)]
print(n)
print(bubbleSort(n))
```