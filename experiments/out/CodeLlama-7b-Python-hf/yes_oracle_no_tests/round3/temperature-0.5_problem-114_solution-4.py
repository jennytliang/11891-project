def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Find the mininum value in the list
    min_value = min(nums)
    # If the minimum value is negative, then we can add it to all values to make a
    # minimal subarray.
    if min_value < 0:
        return min_value * len(nums)
    # If the list is all positive numbers, then the minimum subarray sum is 0
    if all(x >= 0 for x in nums):
        return 0
    # Otherwise, we can find the minimum sum by iterating through the list, and
    # keeping track of the running sum and the current minimum sum
    min_sum = nums[0]
    running_sum = nums[0]
    for i in range(1, len(nums)):
        running_sum += nums[i]
        min_sum = min(running_sum, min_sum)
        running_sum = max(running_sum, 0)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
