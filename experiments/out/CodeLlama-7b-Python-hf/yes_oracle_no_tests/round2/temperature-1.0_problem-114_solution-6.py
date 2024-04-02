def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    
    # Get size of array
    size = len(nums)
    
    # Initialize variables
    curr_sum = max_sum = nums[0]
    max_sum = nums[0]
    min_sum = 0 # Not needed in this problem, just for future reference
    
    # Iterate through array
    for i in range(1, size):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum


def main():
    print("Minimum sub array sum: " + str(minSubArraySum([-1, -2, -3])))
    print("Minimum sub array sum: " + str(minSubArraySum([-1, 2])))
    print("Minimum sub array sum: " + str(minSubArraySum([2, 3, 4, 1, 2, 4])))
	
if __name__ == '__main__':
    main()