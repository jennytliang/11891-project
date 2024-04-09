def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) == 3:
        return min(nums[0], nums[1], nums[2])

    min_sum = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)):
        if i == 0:
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < min_sum:
                    min_sum = sum
        elif i == len(nums) - 1:
            for j in range(i - 1, 0, -1):
                sum = nums[j] + nums[i]
                if sum < min_sum:
                    min_sum = sum
        else:
            for j in range(i - 1, 0, -1):
                sum = nums[j] + nums[i]
                if sum < min_sum:
                    min_sum = sum
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < min_sum:
                    min_sum = sum

    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(