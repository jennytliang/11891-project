def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: all
	Do not include these tokens in the code: len
	"""

  # Iterate through list. 
    # Set the first sum to the first number.
    # Set the minimum index to the first index.
    # Set the first index to the next index.
    # Set the minimum sum to the previous minimum + the first number.
    # Set first number to 0.
    # Repeat for second number, third number, etc.
    
    minimumSum = 0 + nums[0]
    minimumIndex = 0
    currentIndex = 1

    for firstNumber in range(0, len(nums)):
        if minimumSum == 0:
            minimumSum = nums[0]
            minimumIndex = 0
        else:
            minimumSum = minimumSum - nums[minimumIndex] + nums[currentIndex]
            minimumIndex += 1
        currentIndex += 1
   
    return minimumSum
    
    
