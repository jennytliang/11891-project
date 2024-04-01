def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    min_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum

        if current_sum > nums[i]:
            current_sum = nums[i]

    return min_sum


if __name__ == "__main__":
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))
    print(minSubArraySum([-1, -2, -3]))