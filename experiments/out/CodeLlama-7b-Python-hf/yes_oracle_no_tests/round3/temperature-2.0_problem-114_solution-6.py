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

  # Initialize 2 variables to keep track of the best sum so far
  best_sum = float('inf')
  current_sum = 0

  # Loop through the array
  for num in nums:
    current_sum += num
    best_sum = min(best_sum, current_sum)

    # If the current sum is negative, reset it to 0
    if current_sum < 0:
      current_sum = 0

  return best_sum