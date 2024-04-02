def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if nums == []:
        return 0
    min = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
        total += nums[i]
        if total < 0:
            total = nums[i]
        if total < min:
            min = total
    return min


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if nums == []:
        return 0
    min = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
        total += nums[i]
        if total < 0:
            total = nums[i]
        if total < min:
            min = total
    return min


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
