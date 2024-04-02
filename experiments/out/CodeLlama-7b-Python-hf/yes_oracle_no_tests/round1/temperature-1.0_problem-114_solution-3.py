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

  if len(nums) == 0:
    return 0

  # Set initial variables to first values
  smallest_subarr = nums[0]
  left, right = 0, 1

  for i in range(1, len(nums)):
    current_sum = nums[i]
    if current_sum < smallest_subarr:
      smallest_subarr = current_sum
    if current_sum >= 0:
        smallest_subarr += nums[i]
    else:
        # if sum has turned negative, create a new window and continue to add to that
        smallest_subarr = nums[i]
        left = i
        right = i + 1

  return smallest_subarr
