def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code: # Your code here
	"""
    # init
    min_sum = 0
    sum = 0
    for i in nums:
        sum += i
        if sum < 0:
            sum = 0
        if min_sum > sum:
            min_sum = sum
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code: # Your code here
	"""
    # init
    min_sum = 0
    sum = 0
    for i in nums:
        sum += i
        if sum < 0:
            sum = 0
        if min_sum > sum:
            min_sum = sum
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code: # Your code here
	"""
    # init
    min_sum = 0
    sum = 0
    for i in nums:
        sum += i
        if sum < 0:
            sum = 0
        if min_sum > sum:
            min_sum = sum
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
