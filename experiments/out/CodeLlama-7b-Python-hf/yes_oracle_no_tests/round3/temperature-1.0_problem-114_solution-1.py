def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    total = 0
    min_total = 0
    for x in nums:
        total += x
        if total < 0:
            total = 0
        min_total = min(min_total, total)
    return min_total
