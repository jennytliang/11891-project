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
    is_equal_to_sum_odd(7) == True
    is_equal_to_sum_odd(9) == True
    is_equal_to_sum_odd(10) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 10


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(4) == True
    is_equal_to_sum_even_and_odd(6) == True
    is_equal_to_sum_even_and_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8


def is_equal_to_sum_even_and_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive odd number and 3 positive even numbers
    Example
    is_equal_to_sum_even_and_odd_and_three(4) == False
    is_equal_to_sum_even_and_odd_and_three(6) == False
    is_equal_to_sum_even_and_odd_and_three(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8


def is_equal_to_sum_even_and_odd_and_four(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive odd number and 4 positive even numbers
    Example
    is_equal_to_sum_even_and_odd_and_four(4) == False
    is