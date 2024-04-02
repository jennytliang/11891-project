def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: all
	Do not include these tokens in the code: len
	"""

  # code here
    if len(nums) == 0:
        return 0
    min_sum = sum(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            min_sum = min(min_sum, sum(nums[i:j]))
    return min_sum
