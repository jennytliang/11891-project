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
    else:
        mid = (start + end) // 2
        return min(minSubArraySumHelper(nums, start, mid),
                   minSubArraySumHelper(nums, mid + 1, end))
