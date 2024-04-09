def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) < 1:
        return None
    s = 0
    min_sum = nums[0]
    for i in range(len(nums)):
        s += nums[i]
        min_sum = min(s, min_sum)
        if s < 0:
            s = 0
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
