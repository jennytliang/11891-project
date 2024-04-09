def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 0:
        return 0

    # Set up variables
    min_sum = nums[0]
    curr_sum = nums[0]
    
    # Loop through array
    for i in range(1, len(nums)):
        # Check if current sum is greater than previous minimum sum
        if curr_sum > min_sum:
            min_sum = curr_sum
        curr_sum = max(curr_sum, nums[i])
        curr_sum += nums[i]
        
    return min_sum