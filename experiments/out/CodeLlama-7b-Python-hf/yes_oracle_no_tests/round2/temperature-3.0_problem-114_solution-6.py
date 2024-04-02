def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize the minSum variable to the first element in the array
    minSum = nums[0]
    # Initialize the sum variable to 0
    sum = 0
    # For every element in the array
    for x in nums:
        # If the sum is less than 0
        if sum < 0:
            # Set the sum to 0
            sum = 0
        # Add the current element to the sum
        sum += x
        # If the sum is less than the minSum
        if sum < minSum:
            # Set the minSum to the sum
            minSum = sum
    return minSum


# minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
# minSubArraySum([-1, -2, -3]) == -6
print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
