def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  1
	"""

    # init
    min_sum = float('inf')
    curr_sum = 0

    # iterate through list
    for num in nums:
        # add num to curr sum
        curr_sum += num
        # if curr sum is less than min sum, update min sum
        if curr_sum < min_sum:
            min_sum = curr_sum

        # if curr sum is negative, reset curr sum
        if curr_sum < 0:
            curr_sum = 0

    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
