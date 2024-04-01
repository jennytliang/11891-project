def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    num_len = len(nums)
    s = 0
    n = num_len - 1
    min_n = nums[0]

    while s <= n:
        if (nums[s] < min_n):
            min_n = nums[s]
        s = s + 1

    return (min_n)


print(str(minSubArraySum([2, 3, 4, -1, -2, -3])))
