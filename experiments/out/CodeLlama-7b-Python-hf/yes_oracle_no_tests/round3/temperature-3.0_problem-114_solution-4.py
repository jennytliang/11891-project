def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""

    # Initialize variables
    # minSum = 0
    # subArraySum = 0
    minSum = float("inf")
    subArraySum = 0

    # Loop through the list
    for i in range(len(nums)):
        subArraySum += nums[i]

        # Check if subArraySum is less than minSum
        if subArraySum < minSum:
            minSum = subArraySum

        # Check if subArraySum is negative
        if subArraySum < 0:
            subArraySum = 0

    return minSum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
