def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    l = len(nums)
    if l == 0:
        return 0
    if l == 1:
        return nums[0]
    if l == 2:
        return nums[0] + nums[1]
    if l == 3:
        return min(nums[0] + nums[1] + nums[2], nums[0], nums[1], nums[2])

    min_sum = nums[0] + nums[1] + nums[2]
    for i in range(l-2):
        min_sum = min(min_sum, nums[i] + nums[i+1] + nums[i+2])
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6
print(minSubArraySum([-1, -2, -3, -4]))  # -6
print(minSubArraySum([-1, -2, -3, -4, -5]))  # -10
print(minSubArraySum([-1, -2, -3, -4, -5, -6]))  # -16

