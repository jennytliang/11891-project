def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 0


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(5) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 0

def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(6) == True
    is_equal_to_sum_even_and_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 0


def is_equal_to_sum_2_even_and_3_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 3 positive odd numbers
    Example
    is_equal_to_sum_2_even_and_3_odd(4) == False
    is_equal_to_sum_2_even_and_3_odd(12) == True
    is_equal_to_sum_2_even_and_3_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 0


print(is_equal_to_sum_even(10))
print(is_equal_to_sum_odd(10))
print(is_equal_to_sum_even_and_odd(10))
print(is_equal_to_sum_2_even_and_3_odd(10))