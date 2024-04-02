def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

  
    num_of_odd = 0
    num_of_greater_than_10 = 0
    for num in nums:
        if num > 10:
            num_of_greater_than_10 += 1
        if num % 2 != 0:
            num_of_odd += 1

    return num_of_greater_than_10 == num_of_odd


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

  
    num_of_odd = 0
    num_of_greater_than_10 = 0
    for num in nums:
        if num > 10:
            num_of_greater_than_10 += 1
        if num % 2 != 0:
            num_of_odd += 1

    return num_of_greater_than_10 == num_of_odd
