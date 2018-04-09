""" Generate permutations with only adjacent swaps allowed """


def generate(number):
    nums = list(str(number))
    generateHelper(nums, 0, len(nums))


def generateHelper(nums, index, length):
    if index >= length - 1:
        print(''.join(nums))
        return
    generateHelper(nums, index + 1, length)
    swap(nums, index, index + 1)
    generateHelper(nums, index + 2, length)
    swap(nums, index, index + 1)


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


generate(12345)