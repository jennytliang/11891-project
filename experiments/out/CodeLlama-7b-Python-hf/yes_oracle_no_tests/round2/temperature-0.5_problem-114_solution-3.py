def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init values
    # sum of sub array
    sub_sum = 0
    # min sum of sub array
    min_sum = float('inf')
    # loop through nums
    for num in nums:
        # if sub array sum > 0
        if sub_sum > 0:
            # set sub array sum to sub array sum - num
            sub_sum -= num
        else:
            # set sub array sum to sub array sum + num
            sub_sum += num
        # if sub array sum + nums < min sum
        if sub_sum + num < min_sum:
            # set min sum to sub array sum + nums
            min_sum = sub_sum + num
    # return min sum
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
