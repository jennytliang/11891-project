def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code:  ans , odd
	Do not include these tokens in the code: count
	"""

    # write your code here
    ans = 0
    for i in nums:
        if i > 10:
            if (i%10 == 1 or i%10 == 9) and (i//10 == 1 or i//10 == 9):
                ans += 1
    return ans



def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code:  ans , odd
	Do not include these tokens in the code: count
	"""

    # write your code here
    ans = 0
    odd = [1, 3, 5, 7, 9]
    for i in nums:
        if i > 10:
            if i%10 in odd and i//10 in odd:
                ans += 1
    return ans


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code:  ans , odd
	Do not include these tokens in the code: count
	"""

    # write your code here
    ans = 0
    odd = [1,