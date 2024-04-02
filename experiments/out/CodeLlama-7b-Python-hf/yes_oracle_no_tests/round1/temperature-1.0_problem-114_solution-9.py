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

 
class Solution:
    def minSubArraySum(self, nums):
        min_sum = 2**32 - 1
        sum = 0
        x = 0
        for i in range(len(nums)):
            if nums[x] < min_sum:
                min_sum = nums[x]
            sum += nums[i]
            
            if sum < min_sum:
                min_sum = sum
            if sum < 0:
                sum = 0
            x += 1
        return min_sum






s = Solution()
A1_0 = [2, 3, 4, 1]
A2_0 = [1, -1, -1, -1]
print(s.minSubArraySum(A1_0))
print(s.minSubArraySum(A2_0))