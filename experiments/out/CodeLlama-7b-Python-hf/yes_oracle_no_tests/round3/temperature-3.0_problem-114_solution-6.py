def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""

    # iterate through the list and find the min
    # set the min to the first number
    # keep comparing the min to the next number
    # if the next number is less than the min, set the min to the next number
    # continue
    # return the min
    
    min = nums[0]
    for x in range(1, len(nums)):
        if nums[x] < min:
            min = nums[x]
    return min

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
