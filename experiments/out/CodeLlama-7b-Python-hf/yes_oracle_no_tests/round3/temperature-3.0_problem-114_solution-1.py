def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         print(i,j)
    #         print(nums[i:j])
    #         print(sum(nums[i:j]))
    #         if sum(nums[i:j]) < 0:
    #             print(nums[i:j])
    #             break
    #         elif sum(nums[i:j]) == 0:
    #             print(nums[i:j])
    #             break
    #         elif sum(nums[i:j]) == min(nums[i:j]):
    #             print(nums[i:j])
    #             break
    #         elif sum(nums[i:j]) < min(nums[i:j]):
    #             print(nums[i:j])
    #             break
    # print(nums)
    # print(sum(nums))
    # print(min(nums))

    # if sum(nums) < 0:
    #     return sum(nums)

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if sum(nums[i:j]) == 0:
    #             return sum(nums[i:j])
    #         elif sum(nums[i:j]) < 0:
    #             return sum(nums[i:j])
    #         elif sum(nums[i:j]) < min(nums[i:j]):
    #             return sum(nums[i:j])
    # return sum(nums)

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if sum(nums[i:j]) == 0:
    #             return sum(nums[i:j])
    #         elif sum(nums[i:j])