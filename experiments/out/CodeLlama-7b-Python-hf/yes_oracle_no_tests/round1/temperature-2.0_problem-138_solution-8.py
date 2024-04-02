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
    is_equal_to_sum_odd(7) == False
    is_equal_to_sum_odd(9) == False
    is_equal_to_sum_odd(12) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 12


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd and 3 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(8) == False
    is_equal_to_sum_even_and_odd(10) == False
    is_equal_to_sum_even_and_odd(12) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 12
