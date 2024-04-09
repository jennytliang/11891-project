def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Do not include these tokens in the code: # Write your code here .
	"""
    count = 0
    for num in nums:
        if num > 10 and num % 10 % 2 == 1 and num // 10 % 2 == 1:
            count += 1
    return count


def specialFilter(nums):
    return sum(n > 10 and n % 10 % 2 == 1 and n // 10 % 2 == 1 for n in nums)


def specialFilter(nums):
    return sum(n > 10 and n % 10 & 1 == 1 and n // 10 & 1 == 1 for n in nums)
