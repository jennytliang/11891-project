def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    min_sum = 100000000
    current_sum = 0
    for i in nums:
        current_sum += i
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return min_sum


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    min_sum = 100000000
    current_sum = 0
    for i in nums:
        current_sum += i
        if current_sum > 0:
            min_sum = min(current_sum, min_sum)
        else:
            current_sum = 0
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
