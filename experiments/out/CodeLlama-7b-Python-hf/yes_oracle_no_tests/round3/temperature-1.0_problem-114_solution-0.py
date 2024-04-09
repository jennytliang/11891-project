def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Set the initial minimum sum to the first element
    minSum = nums[0]
    # Set the initial sum to the first element
    sum = nums[0]
    # Iterate through the array, starting at the second element
    for i in range(1, len(nums)):
        # If the sum is less than 0, set it to 0
        if sum < 0:
            sum = 0
        # If the sum is less than minSum, set minSum to sum
        if sum < minSum:
            minSum = sum
        # Add the next element to the sum
        sum = sum + nums[i]
    return minSum

# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([-1, -2, 1, -3])) # -2
print(minSubArraySum([1, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, -2])) # -1
print(minSubArraySum([-1, -1])) # -2
