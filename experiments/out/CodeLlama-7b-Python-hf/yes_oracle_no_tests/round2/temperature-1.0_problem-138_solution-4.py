def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: and n % 2 == 0
	"""

    
    ret_val = n % 2 == 0 #check if n is even
    if ret_val: #if n is even, it has to equal sum of 4 even
        s = 0
        i = 1
        while i < 5: #sum 4 evens
            s += i
            i += 2
        if s == n: #equal sum, so return true
            return True
    
    return False #n was not even or sum was unequal 

def is_equal_to_sum_6(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive 6-multiple numbers
    You will not need to check to see if n is divisible by 6.
    Example
    is_equal_to_sum_6(12) == False
    is_equal_to_sum_6(40) == True
    
	Include these tokens in the code: and n % 6 == 0
	"""
    ret_val = n % 6 == 0 #check if n is multiple of 6
    if ret_val: #if n is multiple of 6, it has to equal sum of 4 multiples of 6
        s = 0
        i = 6
        while i < 30: #sum of 4 multiples of 6
            s += i
            i += 6
        if s == n: #equal sum, so return true
            return True
    
    return False #n was not even multiple of 6 or  sum was unequal