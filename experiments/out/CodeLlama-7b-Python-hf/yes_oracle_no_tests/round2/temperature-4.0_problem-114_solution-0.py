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
    sum = 0
    sub_sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < 0:
            sub_sum = sum
        else:
            if sub_sum == 0:
                sub_sum = sum
            elif sub_sum > sum:
                sub_sum = sum
    return sub_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
