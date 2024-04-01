def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # minSubArraySum(nums)
    # nums = [2, 3, 4, 1, 2, 4]
    # nums = [-1, -2, -3]
    
    # 1. Initialize variables
    # min_sum = 1000000000
    # min_sum = float('inf')
    min_sum = max(nums)
    
    # 2. loop through array
    for i in range(len(nums)):
        # 3. initialize sub_array sum
        sub_array_sum = 0
        # 4. loop through sub_array
        for j in range(i, len(nums)):
            # 5. update sum
            sub_array_sum += nums[j]
            # 6. update min_sum
            min_sum = min(min_sum, sub_array_sum)
            # 7. return min_sum
    return min_sum
    
print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))

