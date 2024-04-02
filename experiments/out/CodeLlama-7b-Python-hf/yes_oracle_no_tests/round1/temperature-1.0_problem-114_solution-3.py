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

  # init
  min_sum = float('inf')
  curr_sum = 0

  # loop over the array
  for i in nums:
    curr_sum += i
    min_sum = min(min_sum, curr_sum)
    curr_sum = max(curr_sum, 0)

  return min_sum
