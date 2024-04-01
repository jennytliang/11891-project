def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # Initial conditions
    sum_ = 0
    min_sum = 0

    # Loop through the array
    for num in nums:
        sum_ += num
        if sum_ < min_sum:
            min_sum = sum_
        if sum_ == 0:
            sum_ = 0

    return min_sum


def minSubArraySum_2(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # Initial conditions
    sum_ = 0
    min_sum = 0

    # Loop through the array
    for num in nums:
        sum_ = max(sum_ + num, num)
        min_sum = min(sum_, min_sum)

    return min_sum


print(minSubArraySum_2([2, 3, 4, 1, 2, 4]))
print(minSubArraySum_2([-1, -2, -3]))
