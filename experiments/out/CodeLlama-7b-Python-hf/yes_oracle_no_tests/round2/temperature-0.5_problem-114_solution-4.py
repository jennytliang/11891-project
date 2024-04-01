def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Initialize min_sum
    # Initialize min_length
    # Initialize current_sum
    # Initialize current_length
    # Initialize index
    # Initialize min_index
    # current_sum += nums[index]
    # current_length += 1
    # if current_sum < min_sum
    #     min_sum = current_sum
    #     min_length = current_length
    #     min_index = index
    # index += 1
    # if index == len(nums)
    #     return min_sum, min_length, min_index
    # return min_sum, min_length, min_index
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    # Initialize min_sum
    min_sum = nums[0]
    # Initialize current_sum
    current_sum = nums[0]
    # Initialize current_length
    current_length = 1
    # Initialize index
    index = 1
    # while index < len(nums)
    while index < len(nums):
        # current_sum += nums[index]
        current_sum += nums[index]
        # current_length += 1
        current_length += 1
        # if current_sum < min_sum
        if current_sum < min_sum:
            # min_sum = current_sum
            min_sum = current_sum
        # index += 1
        index += 1
    # return min_sum
    return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))