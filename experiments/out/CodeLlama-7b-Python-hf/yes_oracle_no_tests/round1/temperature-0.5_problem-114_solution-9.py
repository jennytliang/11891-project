def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # Initialize variables
    min_sum = 0
    sum = 0

    # Iterate through the list
    for i in range(0, len(nums)):
        sum += nums[i]
        if sum < 0:
            sum = 0
        if sum < min_sum:
            min_sum = sum

    if min_sum == 0:
        min_sum = min(nums)

    return min_sum


# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([-2, 0, 1, -10, 10]))
