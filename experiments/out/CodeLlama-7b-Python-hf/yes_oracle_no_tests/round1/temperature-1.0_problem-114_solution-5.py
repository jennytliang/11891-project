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

  best = None
  s, e = 0, 0
  sum = 0
  while e < len(nums):
    while s < len(nums) and sum <= 0:
      sum += nums[s]
      s += 1
    while e < len(nums) and sum >= 0:
      sum += nums[e]
      e += 1
    best = min(best, sum)
    sum -= nums[s - 1]
    s += 1
    return best


print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -1, -1, -1, -1, -1])) # -6
