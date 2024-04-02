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
    min_sum = nums[0]
    for num in nums[1:]:
        if num < 0:
            min_sum = min(min_sum, num)
        else:
            min_sum = min(min_sum + num, num)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
