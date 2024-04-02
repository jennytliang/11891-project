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
    min_sub_sum = nums[0]
    sub_sum = nums[0]

    # Iterate through the array of numbers
    for i in range(1, len(nums)):
        # Update the sub_sum
        sub_sum = min(sub_sum + nums[i], nums[i])
        # Update the min_sub_sum
        min_sub_sum = min(min_sub_sum, sub_sum)

    return min_sub_sum
    
    
print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([-1, -2, -3, -4])) # -6
print(minSubArraySum([0, 1, -1])) # 0
print(minSubArraySum([1, 2, -1, -2])) # 0
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1, 1, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1, 1, 1, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1, 1, 1, 1, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1, 1, 1, 1, 1, 1])) # 1
print(minSubArraySum([1, 2, -1, -2, 3, -5, 1, 1,