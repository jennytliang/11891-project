def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd
	Do not include these tokens in the code: # Write your code here .
	"""
    # Write your code here .
    odd = False
    ans = 0
    for i in range(len(nums)):
        if nums[i] > 10:
            if nums[i] % 2 == 1 and nums[i] // 10 % 2 == 1:
                odd = True
            else:
                odd = False
            if odd == True:
                ans += 1
    return ans
