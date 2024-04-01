def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return None
    min_sum = None
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            min_sum = sum(nums[i:j])
    return min_sum        

print(minSubArraySum([1]))
