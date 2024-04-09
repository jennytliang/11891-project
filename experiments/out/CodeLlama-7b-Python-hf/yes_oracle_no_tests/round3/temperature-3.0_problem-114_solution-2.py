def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Your code here
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) > 2:
        return min(minSubArraySum(nums[:2]), minSubArraySum(nums[1:]))



































# def minSubArraySum(nums):
#     """
#     Given an array of integers nums, find the minimum sum of any non-empty sub-array
#     of nums.
#     Example
#     minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
#     minSubArraySum([-1, -2, -3]) == -6
    
# 	Include these tokens in the code: if all ( x >=
# 	"""
#     # Your code here
#     if len(nums) == 0:
#         return 0
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return min(nums[0], nums[1])
#     if len(nums) > 2:
#         return min(minSubArraySum(nums[:2]), minSubArraySum(nums[1:]))























































































































