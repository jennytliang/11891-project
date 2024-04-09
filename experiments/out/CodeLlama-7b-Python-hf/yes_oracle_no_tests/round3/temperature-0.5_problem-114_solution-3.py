def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # initialize variables
    min_sum = 0
    max_sum = 0
    total_sum = 0
    
    # loop over the input
    for num in nums:
        total_sum += num
        max_sum = max(max_sum, total_sum)
        min_sum = min(min_sum, total_sum)
        
    return min_sum
    

