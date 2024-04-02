def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Add your code here
    minSubArraySum = float('inf')
    currSum = 0
    currStart = 0
    for i in range(len(nums)):
        currSum += nums[i]
        while currSum < 0 and currStart < len(nums) - 1:
            currSum -= nums[currStart]
            currStart += 1
        minSubArraySum = min(minSubArraySum, currSum)
    return minSubArraySum
