def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # init
    min = nums[0]
    sum_ = 0
    
    # iterate
    for i in range(len(nums)):
        sum_ += nums[i]
        if sum_ < min:
            min = sum_
        if sum_ < 0:
            sum_ = 0
            
    return min


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
