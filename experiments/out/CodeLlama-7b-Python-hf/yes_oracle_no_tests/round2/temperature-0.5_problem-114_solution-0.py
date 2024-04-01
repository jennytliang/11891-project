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

    # min = nums[0]
    # sum = 0
    # for i in range(len(nums)):
    #     sum += nums[i]
    #     min = min if sum >= min else sum
    #     sum = sum if sum >= 0 else 0

    # return min

    # min = nums[0]
    # sum = 0
    # for i in range(len(nums)):
    #     sum += nums[i]
    #     min = min if sum >= min else sum
    #     sum = sum if sum >= 0 else 0

    # return min

    # min = nums[0]
    # sum = 0
    # for i in range(len(nums)):
    #     sum += nums[i]
    #     min = min if sum >= min else sum
    #     sum = sum if sum >= 0 else 0

    # return min

    min = nums[0]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        min = min if sum >= min else sum
        sum = sum if sum >= 0 else 0

    return min


nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))

nums = [-1, -2, -3]
print(minSubArraySum(nums))
