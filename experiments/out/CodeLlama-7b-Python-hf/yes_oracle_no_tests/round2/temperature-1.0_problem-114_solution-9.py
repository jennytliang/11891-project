def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # A min sum must necessarily include the right end of the array, or the
    # start of the array.
    # We go from the right to left and keep track of the min sum

    start = 0
    left = 0
    right = len(nums) - 1
    last = 0
    sum = 0
    while left <= right:
        sum += nums[left]
        if last < sum:
            last = sum
        if sum < 0:
            start = left
            sum = 0
            left += 1
        elif left == right:
            return last
        else:
            left += 1


print(minSubArraySum([2, 3, 4, 1, 2, 4]), 6)
print(minSubArraySum([-1, -2, -3]), -6)
