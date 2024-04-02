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
    minSubArraySum = 0
    minSum = 0
    sum = 0
    # Loop through array
    for x in nums:
        sum += x
        if sum < minSum:
            minSum = sum
        elif sum > 0:
            minSubArraySum = minSum
    if minSubArraySum == 0:
        minSubArraySum = minSum
    return minSubArraySum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
