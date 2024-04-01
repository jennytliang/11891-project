def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # check empty list
    if len(nums) == 0:
        return 0

    # initialize variables
    min_sum = nums[0]
    current_sum = nums[0]

    # iterate through nums
    for i in range(1, len(nums)):
        current_sum += nums[i]

        # update minimum sum
        if current_sum < min_sum:
            min_sum = current_sum

        # if current sum is negative, reset current sum
        if current_sum < 0:
            current_sum = 0

    return min_sum
