def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize variables
    min_sum = float('inf')
    sub_sum = 0
    i = 0
    while i < len(nums):
        sub_sum += nums[i]
        if sub_sum < min_sum:
            min_sum = sub_sum
        if sub_sum < 0:
            sub_sum = 0
        i += 1
    return min_sum