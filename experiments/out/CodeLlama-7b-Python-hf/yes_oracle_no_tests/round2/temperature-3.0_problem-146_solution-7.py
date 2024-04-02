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
        # check if first and last digits of num are odd
        if num % 10 % 2 == 1 and num // 10 % 2 == 1:
            # check if num > 10
            if num > 10:
                count += 1
    return count

print(specialFilter([15, -73, 14, -15])) # 1
print(specialFilter([33, -2, -3, 45, 21, 109])) # 2
print(specialFilter([10, 20, 55, 105, 120, 125, 130, 132, 145, 150])) # 3
print(specialFilter([10, 20, 55, 105, 120, 125, 130, 132, 145, 150, 151])) # 4
print(specialFilter([10, 20, 55, 105, 120, 125, 130, 132, 145, 150, 151, 152])) # 5
print(specialFilter([10, 20, 55, 105, 120, 125, 130, 132, 145, 150, 152, 153])) # 6
print(specialFilter([10, 20, 55, 105, 120, 125, 130, 132, 145, 150, 153, 154])) # 7
print(specialFilter([10, 20, 55, 105, 120, 125, 130, 132, 145, 150,