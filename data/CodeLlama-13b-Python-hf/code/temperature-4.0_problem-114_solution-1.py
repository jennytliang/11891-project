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
    currSum = sum(nums)  # if everything is negative, just use 2 pointers and return min value over that subarray
    # if there aren't any negatives it's the min value
    minSum = float('inf')

    for pointerEnd in range(len(nums)):
        minSum = currSum
        for subarray in range(1, len(nums)):
            first = nums[:subarray]

            if subarray <= pointerEnd:
                first = nums[pointerEnd -
                             subarray: pointerEnd] if subarray-1 <= pointerEnd-subarray//2 else nums[subarray: pointerEnd]
            elif subarray == pointerEnd:
                return pointerEnd
            currSum = minSum

            minSum = currSum if subarray <= pointerEnd else min(
                currSum, sum(first) )