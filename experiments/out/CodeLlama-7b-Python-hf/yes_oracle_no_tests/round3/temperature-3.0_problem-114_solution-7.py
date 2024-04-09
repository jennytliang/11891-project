def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	Do not include these tokens in the code: # Initialize variables min _
	"""
    cur_sum = 0
    min_sum = 0
    for x in nums:
        cur_sum += x
        if cur_sum < min_sum or min_sum == 0:
            min_sum = cur_sum
        if cur_sum <= 0:
            cur_sum = 0
    return min_sum


# print(minSubArraySum([2, 3, 4, 1, 2, 4]))
# print(minSubArraySum([-1, -2, -3]))


def maxSubArray(nums):
    """
    Given an array of integers nums, find the maximum sum of any non-empty sub-array
    of nums.
    Example
    maxSubArray([2, 3, 4, 1, 2, 4]) == 10
    maxSubArray([-1, -2, -3]) == -1
    maxSubArray([]) == 0
    
	Include these tokens in the code: if all ( x <=
	Do not include these tokens in the code: # Initialize variables max _
	"""
    cur_sum = 0
    max_sum = 0
    for x in nums:
        cur_sum += x
        if cur_sum > max_sum:
            max_sum = cur_sum
        if cur_sum <= 0:
            cur_sum = 0
    return max_sum


# print(maxSubArray([2, 3, 4, 1, 2, 4]))
# print(maxSubArray([-1, -2, -3]))
# print(maxSubArray([]))


def maxProduct(nums):
    """
    Given an array of integers nums, find the maximum product of any non-empty sub-array
    of nums.
    Example
    maxProduct([2, 3, 4, 1, 2, 4]) == 48
    maxProduct([2, -2, -3]) == 24
    maxProduct([-2, 0, -1]) == 0
    
	