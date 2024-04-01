def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    nums_list = list(set(nums))  # removes repeats
    running_sum = 0
    minimum = nums_list[-1]

    # loop nums list
    for x in nums_list:
        running_sum_x = nums_list
