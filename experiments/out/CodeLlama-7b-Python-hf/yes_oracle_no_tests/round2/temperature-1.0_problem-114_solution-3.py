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
    curr_sum = 0
    # Check if array has elements
    if len(nums) > 0:
        # Set current sum to first element
        curr_sum = nums[0]
        # Check if current sum is less than previous minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        # Iterate over the elements of the array
        for i in range(1, len(nums)):
            # Add current element to current sum
            curr_sum += nums[i]
            # Check if current sum is less than previous minimum sum
            if curr_sum < min_sum:
                min_sum = curr_sum
            # Check if current sum is greater than 0
            if curr_sum > 0:
                # Set current sum to 0
                curr_sum = 0
    # Return the minimum sum
    return min_sum


# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([0, 0, 0]))
print(minSubArraySum([1, 1, 1, 1, 1, 1]))
print(minSubArraySum([-1, -1, -1, -1, -1, -1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, -1, 1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, -1, 1, -1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]))
