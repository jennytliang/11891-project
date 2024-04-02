def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    minimumSum = float('inf')
    currentSum = 0 
    for i, x in enumerate(nums):
        currentSum += x
        if currentSum < minimumSum:
            minimumSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return minimumSum

 
def main():
    print(minSubArraySum([-1, -2, -3])) #prints -6


if __name__ == "__main__":
    main()
