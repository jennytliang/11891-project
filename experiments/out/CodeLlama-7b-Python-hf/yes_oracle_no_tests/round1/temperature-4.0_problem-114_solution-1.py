def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    sums = []
    for i in range(len(nums)):
        sums.append(sum(nums[:i+1]))
    sums.append(0)
    return min(sums)


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
