def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if not nums:
        return 0
    min_sum = float('inf')
    sum = 0
    for num in nums:
        sum += num
        if sum < min_sum:
            min_sum = sum
        if sum <= 0:
            sum = 0
    return min_sum
