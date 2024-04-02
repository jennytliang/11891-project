def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    
    mini = sum(nums) - max(nums)
    mini = max(nums) + mini 
	
    return mini
    
print minSubArraySum([2, 3, 4, 1, 2, 4]) #= 1
print minSubArraySum([-1, -2, -3]) #= -6

def minSubArraySum2(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    # Boundary condition
    mini = sum(A)
    mini = max(A) + mini

    for i in range(len(A)):

        current = A[i]

        # current > 0 , we sum this one
        # current + left - right  > 0
        while self.i < i and current + A[self.i] < 0:
            current += A[self.i]
            self.i += 1

        self.i += 1

        # this subArray value + current is smaller than existing
        if current + self.mini > self.mini:
            self.mini += current



