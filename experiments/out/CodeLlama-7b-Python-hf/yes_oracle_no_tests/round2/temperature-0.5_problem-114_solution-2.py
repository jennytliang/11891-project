def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    min_sub_array_sum = nums[0]
    current_sub_array_sum = nums[0]
    for i in range(1, len(nums)):
        current_sub_array_sum = min(current_sub_array_sum + nums[i], nums[i])
        min_sub_array_sum = min(min_sub_array_sum, current_sub_array_sum)
    return min_sub_array_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
