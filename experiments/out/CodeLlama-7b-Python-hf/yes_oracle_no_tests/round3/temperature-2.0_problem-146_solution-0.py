def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans ,
	Do not include these tokens in the code: # write your code
	"""
    ans = 0
    for num in nums:
        if num > 10:
            if num % 10 in (1, 3, 5, 7, 9):
                if num // 10 % 2 == 1:
                    ans += 1
    return ans


print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
print(specialFilter([1, 2, 3, 4, 5]))
print(specialFilter([-1, -2, -3, -4, -5]))
print(specialFilter([11, 22, 33, 44, 55]))
print(specialFilter([-11, -22, -33, -44, -55]))
print(specialFilter([111, 222, 333, 444, 555]))
print(specialFilter([-111, -222, -333, -444, -555]))
print(specialFilter([1111, 2222, 3333, 4444, 5555]))
print(specialFilter([-1111, -2222, -3333, -4444, -5555]))
print(specialFilter([11111, 22222, 33333, 44444, 55555]))
print(specialFilter([-11111, -22222, -33333, -44444, -55555]))
print(specialFilter([111111, 222222, 333333, 444444, 555555]))
print(specialFilter([-111111, -222222, -3333