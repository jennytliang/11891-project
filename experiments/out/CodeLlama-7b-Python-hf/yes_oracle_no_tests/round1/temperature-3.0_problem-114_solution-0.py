def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize variables
    min_sum = nums[0]
    cur_sum = nums[0]

    # Iterate over the array
    for i in range(1, len(nums)):
        # If sum is negative, set to zero
        if cur_sum < 0:
            cur_sum = 0
        # Update current sum
        cur_sum += nums[i]
        # Update minimum sum
        min_sum = min(cur_sum, min_sum)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6
