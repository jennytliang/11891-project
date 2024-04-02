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
    min_sum = 0
    total_sum = 0

    # Loop through the array
    for num in nums:
        total_sum += num

        # If the sum is less than 0, reset the total sum to 0
        if total_sum < 0:
            total_sum = 0

        # If the sum is less than the min_sum, update it
        if total_sum < min_sum or min_sum == 0:
            min_sum = total_sum

    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
