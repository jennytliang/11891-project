def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Approach 1: using two pointers
    if len(nums) < 1:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    # Approach 2: using two pointers
    left, right = 0, 0
    minSum = float('inf')
    curSum = 0
    
    while right < len(nums):
        while curSum < 0 and left < len(nums):
            curSum += nums[left]
            left += 1
        minSum = min(minSum, curSum)
        curSum += nums[right]
        right += 1
    
    return minSum
























