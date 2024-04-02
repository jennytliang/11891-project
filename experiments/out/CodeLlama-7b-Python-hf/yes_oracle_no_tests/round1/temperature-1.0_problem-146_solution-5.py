def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd
	Do not include these tokens in the code: count
	"""
    #code here
    ans = 0
    for num in nums:
        if num > 10:
            odd = (num % 10 == 1 or num % 10 == 9) and (num // 10 % 2 == 1 or num // 10 % 2 == 9)
            if odd:
                ans += 1
    return ans


#test
nums = [15, -73, 14, -15]
#print(specialFilter(nums))

nums = [33, -2, -3, 45, 21, 109]
#print(specialFilter(nums))