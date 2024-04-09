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
    is_equal_to_sum_odd(5) == True
    is_equal_to_sum_odd(6) == False
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 5


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(5) == True
    is_equal_to_sum_even_and_odd(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 5


def is_equal_to_sum_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and 1 positive even number
    Example
    is_equal_to_sum_odd_and_three(4) == False
    is_equal_to_sum_odd_and_three(5) == False
    is_equal_to_sum_odd_and_three(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8


def is_equal_to_sum_even_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and 1 positive even number
    Example
    is_equal_to_sum_even_and_three(4) == True
    is_equal_to_sum_even_and_three(5) == False
    is_equal_to_sum