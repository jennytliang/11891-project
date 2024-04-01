def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    min_val = nums[0]
    min_sum = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] >= min_val:
            min_val = nums[i]
        min_sum = min(min_sum, nums[i] + min_val)
    
    return min_sum


def minSubArraySum2(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        min_sum = min(min_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return min_sum


print(minSubArraySum2([2, 3, 4, 1, 2, 4]))
print(minSubArraySum2([-1, -2, -3]))