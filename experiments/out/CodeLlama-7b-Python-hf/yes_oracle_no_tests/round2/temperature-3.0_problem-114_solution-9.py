def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # initialize variables
    min_sum = float('inf')
    curr_sum = 0
    # loop through the list
    for i in range(len(nums)):
        # add each number to the current sum
        curr_sum += nums[i]
        # if the current sum is less than the min sum, update min sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        # if the current sum is negative, reset the current sum
        if curr_sum < 0:
            curr_sum = 0
    # return the min sum
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([0, 1, 1, 1, 1, 1]))
print(minSubArraySum([-10, 10]))
print(minSubArraySum([-3, -4, -5]))
