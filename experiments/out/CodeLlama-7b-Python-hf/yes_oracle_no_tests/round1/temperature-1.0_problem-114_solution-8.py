def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""

    max = 0
    sum = 0
    for v in nums:
        #print v
        if sum == 0:
            max = v
        sum += v
        if sum < 0:
            sum = 0
        if max < v:
            max = v
    return max



def minSubArraySumTest(input):
    nums = [2, 3, 4, 1, 2, 4]
    output = 1
    output2 = 1
    test = minSubArraySum(nums)
    
    print 'Passes if %s and %s are equal' %(output, test)
    
    nums = [-1, -2, -3]
    output = -6
    output2 = -6
    test2 = minSubArraySum(nums)
    
    print 'Passes if %s and %s are equal' %(output2, test2)

def main():
    minSubArraySumTest(None)
    

if __name__ == '__main__':
	main()
