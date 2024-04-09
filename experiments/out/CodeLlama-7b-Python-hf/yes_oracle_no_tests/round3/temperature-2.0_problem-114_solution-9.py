def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) == 1:
        return nums[0]
    min_ = sum(nums)
    sum_ = 0
    for i in nums:
        sum_ += i
        if sum_ < min_:
            min_ = sum_
        if sum_ < 0:
            sum_ = 0
    return min_


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([-2, -3, -4]))
print(minSubArraySum([-1, -2, -3, -4]))
print(minSubArraySum([-4, -5, -6]))
print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([1, 2, 3, 4, 5]))
print(minSubArraySum([1]))
print(minSubArraySum([-1]))
print(minSubArraySum([-1, 2]))

# Time: O(n)
# Space: O(1)
