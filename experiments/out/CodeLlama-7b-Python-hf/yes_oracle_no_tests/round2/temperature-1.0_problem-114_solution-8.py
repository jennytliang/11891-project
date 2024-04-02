def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    """
	1. Set smallest_sum to a ridiculously high value
	2. traverse the array: 
	a) add the current item to the sum (sum + x)
	b) Compare the sum to the smallest_sum. If the sum is less than smallest, set smallest=sum
	3. Outside the loop: return smallest_sum. 
	
    Time complexity: 0(n) --> linear time. 
    Space Complexity: 0(n) --> O(n) space  --> n iterations. 
    """

    smallest_sum = nums[0] * nums.count()
    sum = 0
    for x in nums:
        sum += x
        smallest_sum = min(smallest_sum, sum)
    
    return smallest_sum
	
print(minSubArraySum([2, 3, 4, 1, 2, 4])
print(minSubArraySum(-2, -3])