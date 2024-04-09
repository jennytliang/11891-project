def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Your code here
    # min_sum = float('inf')
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         current_sum = sum(nums[i:j+1])
    #         if current_sum < min_sum:
    #             min_sum = current_sum
    # return min_sum
    min_sum = float('inf')
    for i in range(len(nums)):
        current_sum = 0
        for j in nums[i:]:
            current_sum += j
            if current_sum < min_sum:
                min_sum = current_sum
    return min_sum



print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))

# 2 3 4 1 2 4
# 1 2 4 3 4 5
# 1 2 4 1 2 4

# 1 2 4 1 2 4
# 1 2 4 1 2 4
# 1 2 4 1 2 4

# 1 2 4 1 2 4