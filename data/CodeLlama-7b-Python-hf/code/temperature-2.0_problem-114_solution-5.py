def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    min_sum = sum(nums)
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = min(current_sum + nums[i], nums[i])
        min_sum = min(min_sum, current_sum)
    return min_sum
