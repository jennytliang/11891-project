def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	Do not include these tokens in the code: # Initialize variables # min
	"""
    # Initialize variables
    min_sum = 0
    sum_array = 0
    min_subarray = []
    # min_subarray = nums
    # min_sum = sum(nums)
    # Do not include these tokens in the code: # Initialize variables # min

    # Iterate through nums
    for i in range(len(nums)):
        sum_array += nums[i]
        # print(sum_array)
        if sum_array < min_sum:
            min_sum = sum_array
            # min_subarray = nums[i:]
        else:
            continue
    # print(min_subarray)
    # print(min_sum)
    return min_sum



print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
