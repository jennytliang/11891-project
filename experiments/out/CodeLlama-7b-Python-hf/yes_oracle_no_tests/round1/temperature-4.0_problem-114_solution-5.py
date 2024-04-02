def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""

    # get minimum of all elements in array
    min_num = min(nums)
    # get maximum of all elements in array
    max_num = max(nums)
    # get sum of all elements in array
    sum_nums = sum(nums)
    
    # if sum of all elements is less than 0, return sum of all elements
    if sum_nums < 0:
        return sum_nums
    # if sum of all elements is greater than 0, return 0
    elif sum_nums > 0:
        return 0
    # if sum of all elements is less than or equal to 0, return max_num - min_num
    else:
        return max_num - min_num
    