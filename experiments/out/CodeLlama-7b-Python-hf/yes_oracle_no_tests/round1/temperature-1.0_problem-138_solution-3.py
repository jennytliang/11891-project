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
    is_equal_to_sum_odd(3) == False
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(7) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 7


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(2) == False
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(6) == False
    is_equal_to_sum_even_and_odd(8) == False
    is_equal_to_sum_even_and_odd(10) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 10


def is_equal_to_sum_even_and_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number, 1 positive odd number and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd_and_three(2) == False
    is_equal_to_sum_even_and_odd_and_three(4) == False
    is_equal_to_sum_even_and_odd_and_three(6) == False
    is_equal_to_sum_even_and_odd_and_three(8) == False
    is_equal_to_sum_even_and_odd_and_three(10) == False
    is_equal_to_sum_even_and_