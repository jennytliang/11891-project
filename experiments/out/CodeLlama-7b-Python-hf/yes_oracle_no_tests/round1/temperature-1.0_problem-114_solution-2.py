def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    """
    Sum up nums, set sum to max, initialize sub as subarray of nums.
    """
    sum_of_nums = sum(nums)
    min_subarray_sum = sum_of_nums # if all nums are negative,
    subarray = []
    
    """
    If nums = None, return None.
    For each number in nums, if subarray sum > sum_of_nums/2, subtract from the
    subarray sum the amount of numbers just added to subarray; this must be a 
    higher order function
    """
    for number in nums:
        subarray.append(number)
        subarray_sum = sum(subarray)
        while subarray_sum > sum_of_nums/2:
            subarray_sum = subarray_sum - subarray[0]
            subarray = subarray[1:]
        min_subarray_sum = min(subarray_sum, min_subarray_sum)
    return min_subarray_sum
    
print minSubArraySum([2,4,1,6,1,7,4,2,5])