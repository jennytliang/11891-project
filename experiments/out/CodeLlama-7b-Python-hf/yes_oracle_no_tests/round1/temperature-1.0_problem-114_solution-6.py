def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init
    min_sum = float('inf')
    start = 0
    end = 0
    # loop
    for i in range(len(nums)):
        min_sum = min(min_sum, sum(nums[start:i+1]))
        if min_sum == sum(nums[start:i+1]):
            start = i
    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))


# 2nd solution
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init
    min_sum = float('inf')
    start = 0
    end = 0
    # loop
    for i in range(len(nums)):
        min_sum = min(min_sum, sum(nums[start:i+1]))
        if min_sum == sum(nums[start:i+1]):
            start = i
    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
