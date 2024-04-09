def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Your code here
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums)
    
    min_sum = nums[0] + nums[1]
    for i in range(1, len(nums)-1):
        min_sum = min(min_sum, nums[i] + nums[i-1])
    
    return min_sum


minSubArraySum([2, 3, 4, 1, 2, 4])