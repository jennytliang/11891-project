def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 0:
        return 0
    min_subarray = nums[0]
    subarray_sum = nums[0]
    for num in nums[1:]:
        subarray_sum = min(subarray_sum + num, num)
        if subarray_sum < min_subarray:
            min_subarray = subarray_sum
    return min_subarray


def minSubArraySum2(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum2([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum2([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 0:
        return 0
    min_subarray = nums[0]
    subarray_sum = nums[0]
    for num in nums[1:]:
        subarray_sum = min(subarray_sum + num, num)
        if subarray_sum < min_subarray:
            min_subarray = subarray_sum
    return min_subarray


def minSubArraySum3(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum3([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum3([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 0:
        return 0
    min_subarray = nums[0]
    subarray_sum = nums[0]
    for num in nums[1:]:
        subarray_sum = min(subarray_sum + num, num