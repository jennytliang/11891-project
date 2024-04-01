def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # Brute Force
    # time complexity: O(n^2)
    # space complexity: O(1)
    # min_sum = 0
    # for i in range(len(nums)):
    #     curr_sum = 0
    #     for j in range(i, len(nums)):
    #         curr_sum += nums[j]
    #         min_sum = min(min_sum, curr_sum)
    # return min_sum

    # Two Pointer Approach
    # time complexity: O(n)
    # space complexity: O(1)
    min_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = min(curr_sum + nums[i], nums[i])
        min_sum = min(min_sum, curr_sum)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
