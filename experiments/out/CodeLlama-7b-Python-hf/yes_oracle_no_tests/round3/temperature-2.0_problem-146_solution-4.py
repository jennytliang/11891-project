def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

  
    odd = lambda x:  x % 2 != 0
    first_last_odd = lambda x: odd(x[0]) and odd(x[-1])
    greater_than_10 = lambda x: x > 10
    filtered = lambda x: filter(first_last_odd, filter(greater_than_10, nums))
    
    return len(list(filtered(nums)))
