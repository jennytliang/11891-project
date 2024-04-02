def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize variables
    # min_sum = 0
    # sum_array = 0
    # num_count = len(nums)
    # for i in range(num_count):
    #     sum_array = sum_array + nums[i]
    #     if i == 0:
    #         min_sum = sum_array
    #     if sum_array < min_sum:
    #         min_sum = sum_array
    #     if sum_array >= 0:
    #         sum_array = 0
    # return min_sum

    # Initialize variables
    # min_sum = 0
    # sum_array = 0
    # num_count = len(nums)
    # for i in range(num_count):
    #     sum_array = sum_array + nums[i]
    #     if i == 0:
    #         min_sum = sum_array
    #     if sum_array < min_sum:
    #         min_sum = sum_array
    #     if sum_array >= 0:
    #         sum_array = 0
    # return min_sum

    # Initialize variables
    min_sum = 0
    sum_array = 0
    num_count = len(nums)
    for i in range(num_count):
        sum_array = sum_array + nums[i]
        if i == 0:
            min_sum = sum_array
        if sum_array < min_sum:
            min_sum = sum_array
        if sum_array >= 0:
            sum_array = 0
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
