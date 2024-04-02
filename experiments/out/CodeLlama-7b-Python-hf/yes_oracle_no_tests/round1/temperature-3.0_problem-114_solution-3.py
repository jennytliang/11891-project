def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 0:
        return 0
    if nums[0] < 0:
        return nums[0]
    if nums[-1] < 0:
        return nums[-1]
    min_sum = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < 0:
            min_sum = min(min_sum, nums[i])
        if nums[i] + nums[i-1] < 0:
            min_sum = min(min_sum, nums[i] + nums[i-1])
        else:
            min_sum = min(min_sum, nums[i] + nums[i-1])
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([1,2,3]))
print(minSubArraySum([1,2,3,4]))
print(minSubArraySum([-1,2,3,4]))
print(minSubArraySum([-1,-2,-3]))
print(minSubArraySum([-1,-2,-3,-4]))
print(minSubArraySum([-2,-1,-3,-4]))
print(minSubArraySum([-1]))
print(minSubArraySum([-1,-2]))
print(minSubArraySum([-1,-2,-3]))
print(minSubArraySum([-1,-2,-3,-4]))
print(minSubArraySum([1,1,1,1,1,1]))
print(minSubArraySum([1,2,3,4,5,6,7]))
print(minSubArraySum([6,6,6,6,6,6]))
print(minSubArraySum([-6,-6,-6,-6,-6,-6]))
print(minSubArraySum([-1,-2,-3,-4,-5,-6]))
print(minSubArraySum([-1