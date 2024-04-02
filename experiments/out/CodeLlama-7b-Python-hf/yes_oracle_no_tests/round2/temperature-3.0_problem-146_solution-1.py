def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

  
    return len([i for i in nums if i > 10 and (int(str(i)[0]) % 2 == 1) and (int(str(i)[-1]) % 2 == 1)])


# def specialFilter(nums):
#     return len([i for i in nums if i > 10 and (i%10)%2 == 1 and (i//10)%2 == 1])

print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
print(specialFilter([-1, 1, 2, 3]))
print(specialFilter([-1, 1, 2, 3, 4, 5]))
print(specialFilter([5, 6, 7, 8, 9, 10]))