def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    min_sub_array_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sub_array_sum = min(current_sum, min_sub_array_sum)
        if current_sum < 0:
            current_sum = 0
    return min_sub_array_sum
