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
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(5) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 5

def is_equal_to_sum_even_or_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd or even numbers
    Example
    is_equal_to_sum_even_or_odd(4) == True
    is_equal_to_sum_even_or_odd(5) == True
    is_equal_to_sum_even_or_odd(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 5

def is_equal_to_sum_even_or_odd_or_zero(n):
    """Evaluate whether the given number n can be written as the sum of exactly 0, 3 positive odd or even numbers
    Example
    is_equal_to_sum_even_or_odd_or_zero(4) == True
    is_equal_to_sum_even_or_odd_or_zero(5) == True
    is_equal_to_sum_even_or_odd_or_zero(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 0

def is_equal_to_sum_four_or_five(n):
    """Evaluate whether the given number n can be written as the sum of exactly 0, 4 or 5 positive odd or even numbers
    Example
    is_equal_to_sum_four_or_five(4) == False
    is_equal_to_sum_four_or_five(5) == True