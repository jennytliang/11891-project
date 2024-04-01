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
    cross_min = minCrossingSum(nums, start, mid, end)
    return min(left_min, right_min, cross_min)


def minCrossingSum(nums, start, mid, end):
    if start == mid:
        return nums[start]
    left_sum = right_sum = float('inf')
    left_curr = right_curr = 0
    for i in range(mid, start - 1, -1):
        left_curr += nums[i]
        if left_curr < left_sum:
            left_sum = left_curr
    for i in range(mid + 1, end + 1):
        right_curr += nums[i]
        if right_curr < right_sum:
            right_sum = right_curr
    return left_sum + right_sum
