def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd
	Do not include these tokens in the code: count
	"""
    ans = 0
    for num in nums:
        if num > 10:
            if num % 10 in {1, 3, 5, 7, 9} and num // 10 in {1, 3, 5, 7, 9}:
                ans += 1
    return ans