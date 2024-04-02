def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: , odd
	"""

   # write code here
    num_greater_10 = 0
    num_special = 0
    
    for num in nums:
        if num > 10:
            num_greater_10+= 1
            
        x = list(str(num))
        
        if x[0] == '1' or x[0] == '3' or x[0] == '5' or x[0] == '7' or x[0] == '9':
            if x[1] == '1' or x[1] == '3' or x[1] == '5' or x[1] == '7' or x[1] == '9':
                num_special+= 1
        
        
    print(f'Special: {num_special}, Greater than 10: {num_greater_10}')        


nums = [15, -73, 14, -15]
specialFilter(nums)

nums1 = [33, -2, -3, 45, 21, 109]
specialFilter(nums)
