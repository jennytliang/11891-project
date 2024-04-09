def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # Find the min sum of all subarrays
    # O(N^2)
    # min_sum = float('inf')
    # for i in range(len(nums)):
    #     for j in range(i, len(nums)):
    #         min_sum = min(min_sum, sum(nums[i:j+1]))
    # return min_sum

    # O(N)
    # min_sum = float('inf')
    # for i in range(len(nums)):
    #     cur_sum = 0
    #     for j in range(i, len(nums)):
    #         cur_sum += nums[j]
    #         min_sum = min(min_sum, cur_sum)
    # return min_sum

    # O(N)
    # min_sum = float('inf')
    # cur_sum = 0
    # for num in nums:
    #     cur_sum += num
    #     min_sum = min(min_sum, cur_sum)
    # return min_sum

    # O(N)
    min_sum = float('inf')
    cur_sum = 0
    for num in nums:
        cur_sum = max(cur_sum + num, num)
        min_sum = min(min_sum, cur_sum)
    return min_sum


print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6
print(minSubArraySum([-10, 1, -10, 1, -10]))  # -20
print(minSubArraySum([-10, -10]))  # -20
print(minSubArraySum([-1, 1]))  # 0
print(minSubArraySum([-1, -1]))  # -2
print(minSubArraySum([0, 0]))  # 0
print(minSubArraySum([0]))  #