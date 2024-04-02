def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""

    for i in range(len(nums), 1, -1):
        for subarray in [[nums[x:x+y] for y in range(0,i-x+1)] for x in range(len(nums))]:
            min_subarray = float('inf')
            for sub in subarray:
                print(sub)
                if sum(sub) < min_subarray:
                    min_subarray = sum(sub)
            print(sum(subarray) // 2)
        return min_subarray
