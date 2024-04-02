def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # if len(nums) == 1:
    #     return min(nums[0],0)
    # elif len(nums) == 2:
    #     return min(nums[0],nums[1],0)
    # else:
    #     return min(nums[0],nums[1],nums[2],minSubArraySum(nums[1:]))
    min_sub_array = nums[0]
    min_sub_array_sum = nums[0]
    for i in range(1, len(nums)):
        min_sub_array_sum = min(nums[i], nums[i] + min_sub_array)
        min_sub_array = min(min_sub_array_sum, min_sub_array)
    return min_sub_array


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
