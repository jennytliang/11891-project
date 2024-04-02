def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # TODO: write an efficient solution
    if len(nums) == 1:
        return nums[0]
    else:
        min_sum = nums[0] + nums[1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                min_sum = min(min_sum, nums[i] + nums[j])
        return min_sum


def minSubArraySum_2(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # TODO: write an efficient solution
    min_sum = nums[0] + nums[1]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            min_sum = min(min_sum, nums[i] + nums[j])
    return min_sum
