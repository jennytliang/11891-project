def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: ...
	"""
    return (n % 2 == 0) and ((n // 2) % 2 == 0)


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(7) == False
    is_equal_to_sum_odd(11) == False
    is_equal_to_sum_odd(12) == True
    
	Do not include these tokens in the code: ...
	"""
    return (n % 2 == 1) and ((n // 2) % 2 == 1)


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and
    2 positive odd numbers
    Example
    is_equal_to_sum_even_odd(4) == True
    is_equal_to_sum_even_odd(6) == True
    is_equal_to_sum_even_odd(12) == False
    
	Do not include these tokens in the code: ...
	"""
    return (n % 2 == 0) and ((n // 2) % 2 == 1)


def is_equal_to_sum_even_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive even numbers
    Example
    is_equal_to_sum_even_even(8) == True
    is_equal_to_sum_even_even(12) == False
    
	Do not include these tokens in the code: ...
	"""
    return (n % 2 == 0) and ((n // 2) % 2 == 0)


def is_equal_to_sum_odd_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and
    2 positive even numbers
    Example
    is_equal_to_sum