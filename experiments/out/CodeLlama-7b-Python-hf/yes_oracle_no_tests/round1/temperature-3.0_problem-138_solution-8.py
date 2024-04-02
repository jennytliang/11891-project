def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8

def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(9) == False
    is_equal_to_sum_odd(12) == False
    is_equal_to_sum_odd(15) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 15

def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_odd(14) == True
    is_equal_to_sum_even_odd(15) == False
    is_equal_to_sum_even_odd(16) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 16

def is_equal_to_sum_odd_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_odd_odd(9) == True
    is_equal_to_sum_odd_odd(10) == False
    is_equal_to_sum_odd_odd(11) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 11

def is_equal_to_sum_even_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive even numbers
    Example
    is_equal_to_sum_even_even(10) == True
    is_equal_to_sum_even_even(12) == False
    is_equal_to_sum_even_even(14) == True
    
	