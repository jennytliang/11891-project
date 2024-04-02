def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Do not include these tokens in the code: # write your code here
	"""
    odd_nums = []

    for num in nums:
        if num > 10:
            if (num % 10) % 2 == 1 and (num // 10) % 2 == 1:
                odd_nums.append(num)

    return len(odd_nums)


print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))


