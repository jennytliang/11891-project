def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

  

    # Write your code here.
    count = 0
    for num in nums:
        if num > 10:
            if num % 10 == 1 or num % 10 == 3 or num % 10 == 5 or num % 10 == 7 or num % 10 == 9:
                if num % 100 // 10 == 1 or num % 100 // 10 == 3 or num % 100 // 10 == 5 or num % 100 // 10 == 7 or num % 100 // 10 == 9:
                    count += 1
    return count
