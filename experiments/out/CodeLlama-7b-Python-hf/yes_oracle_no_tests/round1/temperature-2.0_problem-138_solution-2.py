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
    is_equal_to_sum_odd(9) == True
    is_equal_to_sum_odd(10) == False
    is_equal_to_sum_odd(11) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 9


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and 1 positive even number
    Example
    is_equal_to_sum_even_and_odd(10) == True
    is_equal_to_sum_even_and_odd(11) == False
    is_equal_to_sum_even_and_odd(12) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 12


def is_equal_to_sum_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and 1 positive even number
    Example
    is_equal_to_sum_odd_and_three(10) == False
    is_equal_to_sum_odd_and_three(11) == False
    is_equal_to_sum_odd_and_three(12) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 12


def is_equal_to_sum_even_and_two(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and 2 positive even numbers
    Example
    is_equal_to_sum_even_and_two(10) == True
    is_equal_to_sum_even_and_two(11