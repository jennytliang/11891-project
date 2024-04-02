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
    current_sum = 0
    # Loop through array
    for num in nums:
        current_sum += num
        # Update min_sum if current_sum is smaller
        min_sum = min(min_sum, current_sum)
        # Check if current_sum is negative
        if current_sum < 0:
            current_sum = 0
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([1, 2, -1, -2, 2]))
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, 2, 3, 4, 1, 2, 4]))
print(minSubArraySum([1, 2, 3, 4, -1, 2, 4]))
print(minSubArraySum([1, 2, 3, 4, 1, 2, -4]))
print(minSubArraySum([0, 2, 3, 4, 1, 2, 4]))
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4, -10]))
print(minSubArraySum([0, 2, 3, 4, 1, 2, 4, -10]))
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4, 10]))
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4, 100]))
print(minSubArraySum([1, 2, 3, 4, 1, 2, 4, 100, 1000]))
