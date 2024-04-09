def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    
    # set min_sum to the first element of nums
    min_sum = nums[0]
    
    # set sum to 0
    sum = 0
    
    # loop through nums
    for x in nums:
        # if sum is greater than 0
        if sum > 0:
            # add x to sum
            sum += x
            # if sum is less than min_sum, set min_sum to sum
            if sum < min_sum:
                min_sum = sum
        # otherwise, set sum to x
        else:
            sum = x
            
    return min_sum