def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

   # Initialize list of odd digits
   oddDig = [1, 3, 5, 7, 9]

   # Initialize list of numbers > 10 that satisfy the requirements
   outlst = []

   # Iterate over input list
   for num in nums:
   
       # Get first and last digits of current number
       fDig = num % 10
       lDig = num // 10
       
       # If number greater than 10 and first and last digits both odd...
       if num > 10 and fDig in oddDig and lDig in oddDig:
       
           # Append to output list
           outlst.append(num)
       
   # Return length of output list
   return len(outlst)