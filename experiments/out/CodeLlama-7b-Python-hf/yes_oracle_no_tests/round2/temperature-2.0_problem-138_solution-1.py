def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	"""
    return n % 2 == 0 and n % 4 == 0


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(7) == True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	"""
    return n % 2 == 1 and n % 3 == 0


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even and 2 positive odd numbers
    Example
    is_equal_to_sum_even_odd(4) == False
    is_equal_to_sum_even_odd(10) == True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	"""
    return n % 2 == 0 and n % 4 == 0 and n % 3 == 0


def is_equal_to_sum_even_odd_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even and 3 positive odd numbers
    Example
    is_equal_to_sum_even_odd_odd(5) == False
    is_equal_to_sum_even_odd_odd(14) == True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: if
	"""
    return n % 2 == 0 and n % 4 == 0 and n % 3 == 0 and n % 5 == 0


def is_equal_to_sum_even_even_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_even_even(4) ==