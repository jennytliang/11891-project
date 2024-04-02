def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    """
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        min_sub_sum = nums[0]
        for i in range(1, n):
            if nums[i] + nums[i-1] < nums[i]:
                min_sub_sum = nums[i] + nums[i-1]
            else:
                min_sub_sum = min(min_sub_sum, nums[i])
        return min_sub_sum
    """
    # O(n) time | O(1) space
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        min_sub_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, n):
            current_sum = min(current_sum + nums[i], nums[i])
            min_sub_sum = min(min_sub_sum, current_sum)
        return min_sub_sum


def maxSubArray(nums):
    """
    Given an array of integers nums, find the maximum sum of any non-empty sub-array
    of nums.
    Example
    maxSubArray([2, 3, 4, 1, 2, 4]) == 10
    maxSubArray([-1, -2, -3]) == -1
    
	Include these tokens in the code: if all ( x >=
	"""
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        max_sub_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, n):
            current_sum = max(current_sum + nums[i], nums[i])
            max