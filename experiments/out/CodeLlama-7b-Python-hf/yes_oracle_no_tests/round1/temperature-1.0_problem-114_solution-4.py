def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # minSum = sum(nums)
    minSum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            minSum = min(minSum, sum(nums[i:j+1]))
    return minSum
