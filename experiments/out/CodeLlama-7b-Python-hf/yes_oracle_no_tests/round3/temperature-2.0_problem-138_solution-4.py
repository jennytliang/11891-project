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
    is_equal_to_sum_odd(10) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 10


def is_equal_to_sum_even_or_odd(n):
    """Evaluate whether the given number n can be written as the sum of either 3 positive odd numbers or 4 positive even numbers
    Example
    is_equal_to_sum_even_or_odd(8) == True
    is_equal_to_sum_even_or_odd(12) == True
    is_equal_to_sum_even_or_odd(9) == True
    is_equal_to_sum_even_or_odd(6) == False
    is_equal_to_sum_even_or_odd(10) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 10


def is_equal_to_sum_even_or_odd_or_2(n):
    """Evaluate whether the given number n can be written as the sum of either 3 positive odd numbers or 4 positive even numbers or n == 2
    Example
    is_equal_to_sum_even_or_odd_or_2(8) == True
    is_equal_to_sum_even_or_odd_or_2(12) == True
    is_equal_to_sum_even_or_odd_or_2(9) == True
    is_equal_to_sum_even_or_odd_or_2(6) == False
    is_equal_to_sum_even_or_odd_or_2(10) == True
    is_equal_to_sum_