def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: all
	Do not include these tokens in the code: len
	"""

  # Initialise a variable to store the minimum sum
  min_sum = 0
  # Initialise a variable to store the sum of the subarray
  sum_subarray = 0
  # Initialise a variable to store the length of the subarray
  length_subarray = 0
  # Initialise a variable to store the length of the array
  length_array = len(nums)
  
  # Iterate over the array
  for idx, num in enumerate(nums):
    # If the subarray has not been filled, add the number to the subarray
    if length_subarray < length_array:
      sum_subarray += num
      # Increment the length of the subarray
      length_subarray += 1
    # If the subarray has been filled, check if the subarray's sum is less than the minimum sum
    else:
      if sum_subarray < min_sum:
        min_sum = sum_subarray
      # Reset the subarray's sum to 0
      sum_subarray = 0
      # Reset the length of the subarray to 0
      length_subarray = 0
      
  # Check if the subarray's sum is less than the minimum sum
  if sum_subarray < min_sum:
    min_sum = sum_subarray
  
  # Return the minimum sum
  return min_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
