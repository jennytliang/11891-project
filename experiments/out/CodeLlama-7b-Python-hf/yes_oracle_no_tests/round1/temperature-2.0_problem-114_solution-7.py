def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    #initialize variables
    minSum = 0
    currSum = 0
    #iterate through the array
    for x in nums:
        #add the current element to the sum
        currSum += x
        #if the current sum is less than the current min sum, update the min sum
        if currSum < minSum:
            minSum = currSum
        #if the current sum is greater or equal to the current min sum, update the min sum
        if currSum >= minSum:
            minSum = minSum
    return minSum

def minSubArraySum2(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #initialize variables
    minSum = 0
    currSum = 0
    #iterate through the array
    for x in nums:
        #add the current element to the sum
        currSum += x
        #if the current sum is less than the current min sum, update the min sum
        if currSum < minSum:
            minSum = currSum
        #if the current sum is greater or equal to the current min sum, update the min sum
        if currSum >= minSum:
            minSum = minSum
    return minSum

def minSubArraySum3(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #initialize variables
    minSum = 0
    currSum = 0
    #iterate through the array
    for x in nums:
        #add the current element to the sum
        currSum += x
        #if