def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    nums_min_sum = nums[0]
    nums_total_sum = 0
    for nums_indexes, nums_values in enumerate(nums):
        if nums_indexes == 0:
            nums_total_sum = nums_values
            nums_min_sum = nums_values
        else:
            nums_total_sum = nums_total_sum + nums_values
        if nums_total_sum < nums_min_sum:
            continue
        if nums_indexes > 0:
            nums_min_sum = min(nums_min_sum, nums_total_sum-nums_total_sum/(nums_indexes+1))
    return nums_min_sum
