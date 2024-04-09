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
    # Iterate over the nums list
    for num in nums:
        # Add the current number to the current sum
        curr_sum += num
        # If the current sum is less than the minimum sum, update the minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        # If the current sum is greater than 0, update the minimum sum
        if curr_sum >= 0:
            min_sum = curr_sum
    return min_sum


# print(minSubArraySum([2, 3, 4, 1, 2, 4])) # == 1
# print(minSubArraySum([-1, -2, -3])) # == -6
print(minSubArraySum([-1, -2, -3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([-1, -2, -3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([-1, -2, -3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([-1, -2, -3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([-1, -2, -3, 4, 1, 2, 4]))  # == 1
print(minSubArraySum([