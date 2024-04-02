def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    min_sum = sum(nums)
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub_sum = sum(nums[i:j+1])
            if sub_sum < min_sum:
                min_sum = sub_sum
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
