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
    min_sum = nums[0]
    current_sum = nums[0]
    
    # Iterate through each value in the array
    for i in range(len(nums)):
        # If current sum is greater than the min sum, update min sum
        if current_sum > min_sum:
            min_sum = current_sum
            
        # If the current sum is negative, start a new sum
        if current_sum < 0:
            current_sum = 0
            
        # Add next number to the current sum
        current_sum += nums[i]
        
    # If the current sum is greater than the min sum, update min sum
    if current_sum > min_sum:
        min_sum = current_sum
        
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([0, 1])) # 1
print(minSubArraySum([-1, -2, 1, 2, 3, -1, -1])) # -1
print(minSubArraySum([-3, -5, -8, -4, -10, -1])) # -10
print(minSubArraySum([3, 3, 3])) # 9
print(minSubArraySum([1, 2, 3, 4, 5])) # 15
print(minSubArraySum([-1, -1, -1, -1])) # -4
print(minSubArraySum([1, 1, 1, 1, 1, 1, 1, 1])) # 1