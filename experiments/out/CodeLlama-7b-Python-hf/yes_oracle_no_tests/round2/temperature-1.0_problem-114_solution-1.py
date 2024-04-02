def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""

    # Find minimum subarray sum
    # 1. Initialize minimum subarray sum
    # 2. Loop through array
    # 3. If current number is less than the minimum sum, update minimum sum
    # 4. If current number is greater than or equal to the minimum sum, add the current number to the sum
    # 5. If the sum is greater than the minimum sum, update the minimum sum
    # 6. Return minimum sum
    
    # O(n) time | O(1) space - where n is the length of the input array

    # Initialize minimum subarray sum
    min_sum = float("inf")

    # Loop through array
    for num in nums:
        # If current number is less than the minimum sum, update minimum sum
        if num < min_sum:
            min_sum = num
        # If current number is greater than or equal to the minimum sum, add the current number to the sum
        else:
            min_sum += num
        # If the sum is greater than the minimum sum, update the minimum sum
        if min_sum > 0:
            return min_sum
    # Return minimum sum
    return min_sum

    # Solution explanation:
    # The min_sum serves as a running sum of our subarray.
    # If we encounter a number that is less than the current min_sum, we update the min_sum with the current number.
    # If we encounter a number that is greater than or equal to the current min_sum, we add the current number to the running sum.
    # If the running sum is greater than the min_sum, we update the min_sum with the running sum.
    # We return the min_sum after looping through the entire array.


print(minSubArraySum([2, 3, 4, 1, 2, 4]))
print(minSubArraySum([-1, -2, -3]))
print(minSubArraySum([1, 2, -1, -2, 2]))
print(minSubArraySum([1, 2, -1, -2, -2]))
print(minSubArraySum([1, 1,