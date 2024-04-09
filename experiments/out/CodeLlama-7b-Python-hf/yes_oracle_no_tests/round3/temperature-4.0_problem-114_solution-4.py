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

    if len(nums) == 2:
        return min(nums[0], nums[1])

    min_sum = nums[0] + nums[1]

    for i in range(2, len(nums)):
        # if nums[i] + nums[i - 1] < nums[i - 1] + nums[i - 2]:
        if nums[i] + nums[i - 1] < min_sum:
            min_sum = nums[i] + nums[i - 1]
        else:
            min_sum = nums[i - 1] + nums[i - 2]
    return min_sum


if __name__ == "__main__":
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))
    print(minSubArraySum([-1, -2, -3]))
