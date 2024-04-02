def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Get a starting result of the first element and iterate through the array.
    # Check if our current total so far is greater than or equal to 0. If we
    # are larger than or equal to 0, our current result wins. Else, assign the
    # current total to the result. This results in the cumulative total for every
    # entry in the array.
    result = nums[0]
    runningSum = nums[0] # Used to do the math
    for x in nums[1:]:
      if x >= 0:
        runningSum += x
        if runningSum >= 0:
          result = runningSum
        else:
          runningSum = 0

    # We want to get rid of any possible negative number.
    return result
        
    
#   return sum(nums)      # Just do sum() and watch your test cases break :)

print(minSubArraySum([2, 3, 4, -1, 2, 4]))

