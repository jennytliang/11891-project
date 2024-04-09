def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # initialize some variables
    min_sum = 1000000
    start_index = 0
    end_index = 0
    start_sum = 0
    end_sum = 0

    # iterate through the list, keeping track of the min sum and indices
    for i in range(len(nums)):
        start_sum += nums[i]
        end_sum += nums[i]
        if start_sum < min_sum:
            min_sum = start_sum
            start_index = 0
            end_index = i
        if end_sum < min_sum:
            min_sum = end_sum
            start_index = i
            end_index = len(nums) - 1
        if start_sum > 0:
            start_sum = 0
        if end_sum > 0:
            end_sum = 0

    if min_sum == 1000000:
        return 0
    return nums[start_index : end_index + 1]


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # initialize some variables
    min_sum = 1000000
    start_index = 0
    end_index = 0
    start_sum = 0
    end_sum = 0

    # iterate through the list, keeping track of the min sum and indices
    for i in range(len(nums)):
        start_sum += nums[i]
        end_sum += nums[i]
        if start_sum < min_sum:
            min_sum = start_sum
            start_index = 0
            end_