def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Do not include these tokens in the code:  if len ( num s ) ==  0
	"""

    # Iterative Solution
    """
    total = 0
    min_sum = 2**31 - 1

    for i in range(len(nums)):
        total += nums[i]
        min_sum = min(total, min_sum)

        if total < 0:
            total = 0
    
    return min_sum
    """

    # Recursive Solution
    """
    if len(nums) == 0:
        return 0

    return min(nums[0], minSubArraySum(nums[1:])) + nums[0]
    """

    # Divide & Conquer Solution
    """
    def minSubArraySum(nums, start, end):
        if start == end:
            return nums[start]
        
        mid = (start + end) // 2
        return min(minSubArraySum(nums, start, mid), minSubArraySum(nums, mid + 1, end), minSubArray(nums, start, mid) + minSubArray(nums, mid + 1, end))

    def minSubArray(nums, start, end):
        total = 0
        min_sum = 2**31 - 1

        for i in range(start, end + 1):
            total += nums[i]
            min_sum = min(total, min_sum)

            if total < 0:
                total = 0
        
        return min_sum
    """

    # Dynamic Programming Solution
    """
    total = 0
    min_sum = 2**31 - 1

    for i in range(len(nums)):
        total += nums[i]
        min_sum = min(total, min_sum)

        if total < 0:
            total = 0
    
    return min_sum
    """

    # Optimized Dynamic Programming Solution
    """
    total = 0
    min_sum = 2**31 - 1

    for i in range(len(num