def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums)==1:
        return nums[0]
        
    curr_sum = 0
    min_sum = abs(nums[0]+nums[1])
    for i in range(len(nums)):
        curr_sum+=nums[i]
        curr_sum = max(curr_sum,0)
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum <0:
            curr_sum = 0
    return min_sum**2
    
    
print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))