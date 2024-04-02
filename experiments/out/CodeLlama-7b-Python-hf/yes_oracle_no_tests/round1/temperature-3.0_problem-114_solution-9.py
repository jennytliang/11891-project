def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Find the minimum sum of any subarray
    # Initialize the minimum sum of any subarray to be the sum of the first subarray
    min_sum = sum(nums[0:3])
    # For every subarray in the array,
    for i in range(len(nums)):
        # For every subarray of length 3,
        for j in range(i, i + 3):
            # If the subarray is not empty,
            if j < len(nums):
                # Find the sum of the subarray
                subarray_sum = sum(nums[i:j])
                # If this subarray is the smallest so far,
                if min_sum > subarray_sum:
                    # Update the minimum sum
                    min_sum = subarray_sum
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
