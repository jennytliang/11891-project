def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Your code here
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    max_sum = nums[0]
    min_sum = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
        total += nums[i]
        if total < 0:
            total = 0
        if total < min_sum:
            min_sum = total
        if total > max_sum:
            max_sum = total
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Your code here
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    min_sum = nums[0]
    max_sum = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
        total += nums[i]
        if total < 0:
            total = 0
        if total < min_sum:
            min_sum = total
        if total > max_sum:
            max_sum = total
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
