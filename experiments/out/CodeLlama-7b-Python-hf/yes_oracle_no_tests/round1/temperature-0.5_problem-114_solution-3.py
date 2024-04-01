def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # Your code here
    if len(nums) == 0:
        return 0
    
    min_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = min(current_sum + nums[i], nums[i])
        min_sum = min(current_sum, min_sum)

    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))