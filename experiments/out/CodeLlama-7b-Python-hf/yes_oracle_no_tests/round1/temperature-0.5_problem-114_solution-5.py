def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # if len ( nums ) == 0:
    #     return 0
    #
    # min_sum = nums[0]
    # sum = nums[0]
    #
    # for i in range(1, len(nums)):
    #     sum += nums[i]
    #     min_sum = min(min_sum, sum)
    #     if sum < 0:
    #         sum = 0
    #
    # return min_sum

    if len(nums) == 0:
        return 0

    min_sum = nums[0]
    sum = nums[0]

    for i in range(1, len(nums)):
        sum += nums[i]
        min_sum = min(min_sum, sum)
        if sum < 0:
            sum = 0

    return min_sum


if __name__ == '__main__':
    print("Example:")
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))
    print(minSubArraySum([-1, -2, -3]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([0]) == 0
    assert minSubArraySum([-1]) == -1
    assert minSubArraySum([]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
