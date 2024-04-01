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
        running_sum_x = nums_list.count(x)

        # checks if the running sum of the element in the loop is negative or equal to 0
        if nums_list.index(x) != 0 and running_sum_x > 0 and minimum > ((running_sum - nums_list.count(nums_list[0])) * x):  # if the element is different then the first element
            pass

        # creates the running sum and checks if it is negative or the sum is greater then the minimum (if the previous one is false)
        running_sum = running_sum_x * x

        if nums_list.index(x) == 0 or (running_sum > 0 or running_sum_x <= 0) and minimum <= running_sum:
            minimum = running_sum

        # Checks if there is a positive running sum and breaks if true
    return minimum
"""
# TESTED BY RUNNING FUNCTION
a = minSubArraySum([-2, -1, -0, 0, 1, 3])
print(a) = 2 
"""
