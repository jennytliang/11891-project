def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize all variables we'll need
    current_sum = 0
    min_sum = 0xFFFFFFFF
    min_idx = None
  
    # Start with the first index and go until end of array with +1
    for idx, value in enumerate(nums):
        # If the current sum is less than min sum, update min sum and index accordingly
        if current_sum < min_sum:
            min_sum = current_sum
            min_idx = idx

        # Add to current sum. If it's less than zero, reset to zero
        current_sum += value
        if current_sum < 0:
            current_sum = 0        

    return min_sum
    return min_idx

def minSubArraySum_1(nums):
    left = idx = 0
    sumSubArray = nums[0]
    for i in range(0, len(nums)):
        sumSubArray = min(sumSubArray + nums[i], nums[i])
        idx = i
        if sumSubArray < 0:
            sumSubArray = nums[i + 1]
            left = i + 1
    return(sumSubArray, left, idx)
        
def minSubArraySum_2(nums):
    minSum = 0xFFFFFFFF
    left, idx = nums[0], 0
    for i, v in enumerate(nums):
        minSum = min(v, minSum + v)
        if minSum < 0:
            left = i + 1
        idx = i
    return(minSum, left, idx)