def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize variables
    min_sum = float('inf')
    start_index = 0
    end_index = 0
    subarray_sum = 0

    # Loop through the array
    for i in range(len(nums)):
        # Add the current value to the sum
        subarray_sum += nums[i]
        # If the sum is less than the minimum sum, update the minimum sum
        if subarray_sum < min_sum:
            min_sum = subarray_sum
            # Reset the start and end index
            start_index = i
            end_index = i
        # If the sum is equal to the minimum sum, update the end index
        elif subarray_sum == min_sum:
            end_index = i

        # If the sum is greater than the minimum sum, reset the sum and start index
        elif subarray_sum > min_sum:
            subarray_sum = 0
            start_index = i

    # Return the minimum sum and the indices
    return min_sum, start_index, end_index


nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))
