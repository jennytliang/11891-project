def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize the minimum sum to the sum of the whole array
    min_sum = sum(nums)
    # Iterate through the indices of the array
    for i in range(len(nums)):
        # Iterate through the indices of the array starting from the index of the current iteration
        for j in range(i, len(nums)):
            # Sum the subarray
            sub_sum = sum(nums[i:j+1])
            # If the subarray is greater than the current minimum sum, update the minimum sum
            if sub_sum > min_sum:
                min_sum = sub_sum
    return min_sum


if __name__ == "__main__":
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))
    print(minSubArraySum([-1, -2, -3]))
