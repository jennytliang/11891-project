def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # find the min value
    min_num = min(nums)
    # find the sum of all nums
    sum_nums = sum(nums)
    
    # if the sum of all nums is less than the min value
    if sum_nums < min_num:
        # return the sum of all nums
        return sum_nums
    
    # if the sum of all nums is greater than or equal to the min value
    else:
        # return the min value
        return min_num
    
print(minSubArraySum([2, 3, 4, 1, 2, 4])) # 1
print(minSubArraySum([-1, -2, -3])) # -6
print(minSubArraySum([1, 1, 1, 1, 1, 1])) # 1
print(minSubArraySum([-1, -2, -3, -10, -10, -10])) # -10
print(minSubArraySum([-10, -10, -10, -10])) # -10