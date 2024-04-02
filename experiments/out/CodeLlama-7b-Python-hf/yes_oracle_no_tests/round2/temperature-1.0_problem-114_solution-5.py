def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code: # code here
	"""
    # Your code here
    # min_sum = nums[0]
    # for i in range(1, len(nums)):
    #     min_sum = min(nums[i], min_sum+nums[i])
    # return min_sum
    min_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = min(current_sum+nums[i], nums[i])
        min_sum = min(min_sum, current_sum)
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code: # code here
	"""
    # Your code here
    min_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        if current_sum > 0:
            current_sum = nums[i]
        else:
            current_sum += nums[i]
        min_sum = min(min_sum, current_sum)
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code: # code here
	"""
    # Your code here
    min_sum = nums[0]
    current_sum = nums[0]
    for i in