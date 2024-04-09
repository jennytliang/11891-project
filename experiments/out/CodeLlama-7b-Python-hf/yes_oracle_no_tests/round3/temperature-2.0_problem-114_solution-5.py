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

  # # Method 1: Brute Force
  # # O(n^2) time | O(1) space
  # def minSubArraySum(nums):
  #     min_sum = float("inf")
  #     for i in range(len(nums)):
  #         for j in range(i, len(nums)):
  #             min_sum = min(min_sum, sum(nums[i:j+1]))
  #     return min_sum

  # Method 2: Two Pointers
  # O(n) time | O(1) space
  def minSubArraySum(nums):
      min_sum = float("inf")
      left = 0
      right = 0
      cur_sum = 0
      while right < len(nums):
          cur_sum += nums[right]
          min_sum = min(min_sum, cur_sum)
          while cur_sum < 0 and left < right:
              cur_sum -= nums[left]
              left += 1
          right += 1
      return min_sum

  return minSubArraySum(nums)


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
