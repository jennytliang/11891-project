def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    return minSubArraySumHelper(nums, 0, len(nums) - 1)


def minSubArraySumHelper(nums, start, end):
    if start == end:
        return nums[start]
    mid = (start + end) // 2
    left_min = minSubArraySumHelper(nums, start, mid)
    right_min = minSubArraySumHelper(nums, mid + 1, end)
    return min(left_min, right_min)


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))