def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # keep track of the sum of the array
    # keep track of the minimum sum, starting at infinity
    # iterate through the array
    # if the sum is greater than the current minimum, set the current minimum to the sum
    # if the sum is less than the current minimum, add the number to the sum
    # if the sum is less than the current minimum, set the sum to the number
    # if the sum is greater than the current minimum, do nothing
    # return the minimum sum
    # O(n) time and space
    # 45 ms
    # 14.2 MB
    # 88.11%
    # 71.54%
    
    # if len(nums) == 0:
    #     return 0
    
    # sum = nums[0]
    # current_min = sum
    # for i in range(1, len(nums)):
    #     sum += nums[i]
    #     if sum < current_min:
    #         current_min = sum
    # return current_min
    
    # O(n) time and space
    # 36 ms
    # 13.9 MB
    # 88.11%
    # 90.27%
    
    # if len(nums) == 0:
    #     return 0
    
    # current_min = nums[0]
    # for i in range(1, len(nums)):
    #     current_min = min(current_min + nums[i], nums[i])
    # return current_min
    
    # O(n) time and space
    # 40 ms
    # 13.9 MB
    # 88.11%
    # 96.91%
    
    # if len(nums) == 0:
    #     return 0
    
    # current_min = nums[0]
    # for i in range(1, len(nums)):
    #     current_min = min(current_min + nums[i], num