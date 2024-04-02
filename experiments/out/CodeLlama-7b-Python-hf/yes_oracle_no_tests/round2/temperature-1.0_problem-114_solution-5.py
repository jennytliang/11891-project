def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    curr = [0]

    n = len(nums)

    for i in range(n):
        curr[i] += curr[i - 1] + nums[i]
    #print(nums)
    #print(str(curr))
    
    curr.append(0)
    for i in range(1, n + 1):
        if (curr[i] == 0):
            curr[i] += nums[i - 1]
            #print(str(curr))
        #if curr[i - 1] >= 0:
        #    curr[i] += curr[i-1]
        #if curr[i] > 0 and curr[i - 1] == 0:
        #    curr[i] += nums[i-1]
    #print(str(curr))
    return(min(curr))


print(str(minSubArraySum((3, 4, -1, 5, 5, 3))))