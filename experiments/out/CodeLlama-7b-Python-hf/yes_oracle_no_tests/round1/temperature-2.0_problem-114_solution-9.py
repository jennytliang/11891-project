def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # initialize an empty list to hold the sums of the subarrays
    subarray_sums = []
    # initialize a variable to hold the smallest subarray sum
    smallest_sum = float('inf')
    # initialize a variable to hold the current subarray sum
    current_sum = 0
    # for each number in the list
    for num in nums:
        # add the number to the current sum
        current_sum += num
        # if the current sum is less than the smallest sum
        if current_sum < smallest_sum:
            # set the smallest sum to the current sum
            smallest_sum = current_sum
        # if the current sum is 0
        if current_sum == 0:
            # add the number to the subarray sums
            subarray_sums.append(num)
        # otherwise
        else:
            # add the number to the subarray sums
            subarray_sums.append(current_sum)
    # return the smallest sum
    return smallest_sum

print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([-2, -3, -1])) # -2
print(minSubArraySum([0, -1, -2, -3])) # -1
print(minSubArraySum([-1, 0, -2, -3])) # -1
print(minSubArraySum([-1, -2, 0, -3])) # -1
print(minSubArraySum([-1, -2, -3, 0])) # -1
print(minSubArraySum([-2, -1, 0, -3])) # -1
print(minSubArraySum([-2, -1, -3, 0])) # -1
print(minSubArraySum([-2, -1, -3, -1])) # -1
print(minSubArraySum([-2, -1, -3, -1, 0])) # -1
print(minSubArraySum([-2