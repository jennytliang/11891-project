def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # min = 0
    # if len(nums) == 0:
    #     return 0
    # for i in range(len(nums)):
    #     min = min + nums[i]
    #     min = min if min < 0 else 0
    # return min

    min = 0
    max = 0
    for i in range(len(nums)):
        min = min + nums[i]
        max = max if max > min else min
        min = min if min < 0 else 0
    return max


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
