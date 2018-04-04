

def maxProductSubArray(nums):

    maxSoFar = 0
    maxEndingHere = nums[0]
    minEndingHere = nums[0]

    for num in nums[1:]:
        maxEndingHere = max(maxEndingHere*num, minEndingHere*num, num)
        minEndingHere = min(maxEndingHere*num, minEndingHere*num, num)
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar


if __name__ == '__main__':
    input = [-6,-3,8,-9,-1,-1,3,6,9,0,3,-1]
    print(maxProductSubArray(input))