def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Iterative Solution
    # min = 0
    # for i in range(len(nums)):
    #     if min > sum(nums[i:]):
    #         min = sum(nums[i:])
    # return min

    # Recursive Solution
    # def minSubArraySum(nums, i, j, min):
    #     if i > j:
    #         return min
    #     if min > sum(nums[i:j + 1]):
    #         min = sum(nums[i:j + 1])
    #     return minSubArraySum(nums, i + 1, j, min)
    # return minSubArraySum(nums, 0, len(nums) - 1, 0)

    # One-liner
    return min(nums[i:j + 1] for i in range(len(nums)) for j in range(i, len(nums)))


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Iterative Solution
    # min = 0
    # for i in range(len(nums)):
    #     if min > sum(nums[i:]):
    #         min = sum(nums[i:])
    # return min

    # Recursive Solution
    # def minSubArraySum(nums, i, j, min):
    #     if i > j:
    #         return min
    #     if min > sum(nums[i:j + 1]):
    #         min = sum(nums[i:j + 1])
    #     return minSubArraySum(nums, i + 1, j