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
    min_sum = nums[0]
    current_sum = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        current_sum += nums[i]
        # If the current sum is less than the min sum
        if current_sum < min_sum:
            min_sum = current_sum
        # If the current sum is greater than or equal to the min sum
        if current_sum >= min_sum:
            current_sum = 0
            
    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([-1, 1]))
print(minSubArraySum([-1, 1, 1]))
print(minSubArraySum([-1, 1, -1]))
print(minSubArraySum([-1, 1, -1, 1]))
print(minSubArraySum([-1, 1, -1, 1, -1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, 1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, 1, -1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, 1, -1, 1]))
print(minSubArraySum([-1, 1, -1, 1, -1, 1, 1, -1, 1, -1]))









































































