def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 0 and str(n % 2)+""+str(0)
    #return n % 2==0 # return True if integer n is even, False if n is odd.
        
"""Unit Tests"""
print is_equal_to_sum_even(8)
print is_equal_to_sum_even(4)
print is_equal_to_sum_even(6)