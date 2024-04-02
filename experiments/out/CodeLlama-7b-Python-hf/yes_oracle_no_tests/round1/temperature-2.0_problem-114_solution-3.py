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
    # Set the minimum sum to the first element of the array
    min_sum = nums[0]
    # Set the sum of the subarray to the first element of the array
    subarray_sum = nums[0]
    # Set the index of the end of the subarray to 0
    subarray_end = 0

    # Loop through the array
    for i in range(1, len(nums)):
        # If the subarray sum is greater than the minimum sum
        if subarray_sum > min_sum:
            # Set the minimum sum to the subarray sum
            min_sum = subarray_sum

        # If the current element is less than the subarray sum
        if nums[i] < subarray_sum:
            # Reset the subarray sum to the current element
            subarray_sum = nums[i]
            # Set the end of the subarray to the current index
            subarray_end = i

        # If the current element is greater than the subarray sum
        if nums[i] >= subarray_sum:
            # Add the current element to the subarray sum
            subarray_sum += nums[i]

    # Print the minimum sum
    print(min_sum)


# Test case 1
minSubArraySum([2, 3, 4, 1, 2, 4])
# Expected result: 1
# Test case 2
minSubArraySum([-1, -2, -3])
# Expected result: -6
