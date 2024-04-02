def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # if len(nums) == 1:
    #     return nums[0]
    # if len(nums) == 2:
    #     return min(nums[0], nums[1])
    # if len(nums) == 3:
    #     return min(nums[0], nums[1], nums[2])
    # if len(nums) == 4:
    #     return min(nums[0], nums[1], nums[2], nums[3])
    # if len(nums) == 5:
    #     return min(nums[0], nums[1], nums[2], nums[3], nums[4])
    # if len(nums) == 6:
    #     return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])

    # nums = [-1, -2, -3]
    # nums = [1, 2, 3, 4, 1, 2, 4]

    # for i in range(len(nums)):
    #     if nums[i] < nums[i+1]:
    #         nums[i], nums[i+1] = nums[i+1], nums[i]
    # return nums

    # nums = [-1, -2, -3]
    # nums = [1, 2, 3, 4, 1, 2, 4]

    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         nums[i], nums[j] = nums[j], nums[i]
    # return nums

    nums = [-1, -2, -3]
    nums = [1, 2, 3, 4, 1, 2, 4]

    for i in range(len(nums) - 1