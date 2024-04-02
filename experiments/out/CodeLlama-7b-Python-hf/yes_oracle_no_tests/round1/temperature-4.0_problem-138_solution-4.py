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


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive even numbers and exactly 1 positive odd number
    Example
    is_equal_to_sum_even_odd(4) == False
    is_equal_to_sum_even_odd(5) == False
    is_equal_to_sum_even_odd(8) == True
    is_equal_to_sum_even_odd(9) == True
    
    Include these tokens in the code: return n >=
    """
    return n >= 8


def is_equal_to_sum_even_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_even(4) == False
    is_equal_to_sum_even_even(8) == True
    is_equal_to_sum_even_even(12) == True
    
    Include these tokens in the code: return n >=
    """
    return n >= 8


def is_equal_to_sum_odd_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers
    Example
    is_equal_to_sum_odd_odd(4) == False
    is_equal_to_sum_odd_odd(5) == True
    is_equal_to_sum_odd_odd(8) == False
    
    In