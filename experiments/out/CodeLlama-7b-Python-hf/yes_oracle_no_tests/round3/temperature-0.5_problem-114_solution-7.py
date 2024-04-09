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
    # if len(nums) == 1:
    #     return nums[0]
    # if len(nums) == 2:
    #     return min(nums[0], nums[1])
    # if len(nums) == 3:
    #     return min(nums[0], nums[1], nums[2])
    # if len(nums) == 4:
    #     return min(nums[0], nums[1], nums[2], nums[3])

    # # for loop
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         if sum(nums[i:j]) == min(sum(nums[i:j])):
    #             return sum(nums[i:j])

    # # recursive
    # def min_sum(i, j):
    #     if i == j:
    #         return nums[i]
    #     else:
    #         return min(nums[i], nums[i] + min_sum(i + 1, j))

    # return min_sum(0, len(nums) - 1)

    # dynamic programming
    sum_array = [nums[0]]
    for i in range(1, len(nums)):
        sum_array.append(nums[i] + sum_array[i - 1])

    min_sum = sum_array[0]
    for i in range(1, len(sum_array)):
        if sum_array[i] < min_sum:
            min_sum = sum_array[i]

    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
