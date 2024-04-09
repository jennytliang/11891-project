def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initializing the minimum sum value
    min_sum = float('inf')

    # Initializing the start and end pointers
    start = 0
    end = 0

    # Initializing the running sum
    running_sum = 0

    # Looping through the array
    for i in range(len(nums)):
        # Adding the value at the current index to the running sum
        running_sum += nums[i]

        # If the running sum is less than the minimum sum we've seen so far, we update the minimum sum
        if running_sum < min_sum:
            min_sum = running_sum

        # If the running sum is greater than zero, we update the end pointer
        if running_sum > 0:
            end = i

        # If the running sum is less than zero, we update the start pointer
        if running_sum < 0:
            start = i + 1

    # Returning the minimum sum
    return min_sum
