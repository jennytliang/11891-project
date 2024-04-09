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
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers
    Example
    is_equal_to_sum_odd(2) == True
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 6


def is_equal_to_sum_four(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive numbers
    Example
    is_equal_to_sum_four(4) == True
    is_equal_to_sum_four(6) == True
    is_equal_to_sum_four(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8


def is_equal_to_sum_five(n):
    """Evaluate whether the given number n can be written as the sum of exactly 5 positive numbers
    Example
    is_equal_to_sum_five(4) == False
    is_equal_to_sum_five(6) == True
    is_equal_to_sum_five(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 10


def is_equal_to_sum_n(n, n_sum):
    """Evaluate whether the given number n can be written as the sum of exactly n positive numbers
    Example
    is_equal_to_sum_n(4, 4) == True
    is_equal_to_sum_n(4, 6) == False
    is_equal_to_sum_n(6, 4) == False
    is_equal_to_sum_n(6, 6) == True
    is_equal_to_sum_n(8, 4) == False
    is_equal_to