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
    sum = 0
    minSum = 0
    #loop through the array
    for x in nums:
        sum += x
        #check if sum is greater than zero, then update minSum
        if sum >= 0:
            minSum = sum
        #if the sum is less than zero, then update the sum to zero
        else:
            sum = 0
    return minSum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
