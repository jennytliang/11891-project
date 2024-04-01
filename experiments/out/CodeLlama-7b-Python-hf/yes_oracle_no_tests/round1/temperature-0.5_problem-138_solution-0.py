def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=  8 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 8 and n % 2 == 0 and (n - 8) % 4 == 0



def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(13) == False
    is_equal_to_sum_odd(14) == True
    
	Include these tokens in the code: return n >= 14 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 14 and n % 2 == 1 and (n - 14) % 4 == 0



def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers and exactly 4 positive odd numbers
    Example
    is_equal_to_sum_even_odd(14) == False
    is_equal_to_sum_even_odd(26) == False
    is_equal_to_sum_even_odd(28) == True
    
	Include these tokens in the code: return n >= 28 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 28 and n % 2 == 0 and (n - 28) % 8 == 0



def is_equal_to_sum_odd_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers and exactly 4 positive even numbers
    Example
    is_equal_to_sum_odd_even(14) == False
    is_equal_to_sum_odd_even(26) == False
    is_equal_to_sum_odd_even(28) == True
    
	Include these tokens in the code: return n >= 28 and
	Do not include these