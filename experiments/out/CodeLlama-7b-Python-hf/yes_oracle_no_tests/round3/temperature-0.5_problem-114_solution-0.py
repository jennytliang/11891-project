def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init vars
    minSum = 0
    currentSum = 0
    # iterate through nums
    for num in nums:
        currentSum += num
        if currentSum < minSum or minSum == 0:
            minSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return minSum


def minSubArraySum2(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum2([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum2([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init vars
    minSum = 0
    currentSum = 0
    # iterate through nums
    for num in nums:
        currentSum += num
        if currentSum < minSum or minSum == 0:
            minSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return minSum


def minSubArraySum3(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum3([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum3([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init vars
    minSum = 0
    currentSum = 0
    # iterate through nums
    for num in nums:
        currentSum += num
        if currentSum < minSum or minSum == 0:
            minSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return minSum


def minSubArraySum4(nums):
    """
    Given an array of