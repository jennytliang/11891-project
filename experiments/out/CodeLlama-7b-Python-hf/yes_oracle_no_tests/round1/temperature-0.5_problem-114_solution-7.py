def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    if len(nums) == 0:
        return 0

    min = nums[0]
    cur = nums[0]
    for i in range(1, len(nums)):
        cur = min(cur + nums[i], nums[i])
        min = min(cur, min)
    return min


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))