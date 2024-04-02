def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # min_sum = nums[0]
    # for i in range(1, len(nums)):
    #     min_sum = min(min_sum, nums[i] + nums[i - 1])
    # return min_sum

    min_sum = nums[0]
    for i in range(1, len(nums)):
        min_sum = min(min_sum, nums[i] + nums[i - 1])
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
