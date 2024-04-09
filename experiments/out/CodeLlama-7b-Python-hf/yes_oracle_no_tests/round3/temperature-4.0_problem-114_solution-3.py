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
        return None
    if len(nums) == 1:
        return nums[0]
    # initialize the minSum to a large value
    minSum = 1000000000
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            # check the subarray
            if nums[i:j + 1][0] >= 0:
                # add all the elements in the array
                minSum = min(minSum, sum(nums[i:j + 1]))
            else:
                # if the first element is negative, add it to the minSum
                minSum = min(minSum, nums[i:j + 1][0])
    return minSum


minSubArraySum([2, 3, 4, 1, 2, 4])
