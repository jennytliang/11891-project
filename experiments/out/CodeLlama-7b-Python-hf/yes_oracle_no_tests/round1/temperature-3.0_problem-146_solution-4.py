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
    
    # A: init answer
    ans = 0
    
    # B: iterate over nums
    for num in nums:
        
        # C: check condition
        if num > 10:
            
            # D: check if first and last digits are odd
            if num % 10 in [1, 3, 5, 7, 9]:
                
                # E: update answer if condition is met
                ans += 1
    
    # F: return answer
    return ans


print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
