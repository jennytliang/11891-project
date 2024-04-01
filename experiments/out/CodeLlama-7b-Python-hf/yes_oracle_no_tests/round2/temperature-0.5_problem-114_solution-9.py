def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	Do not include these tokens in the code: # Initialize variables min
	"""
    curSum = 0
    minSum = float('inf')

    for num in nums:
        curSum += num
        minSum = min(curSum, minSum)
        if curSum < 0:
            curSum = 0

    return minSum