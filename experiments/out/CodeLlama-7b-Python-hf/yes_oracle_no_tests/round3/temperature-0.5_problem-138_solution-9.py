def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    n_even = n / 2
    return n_even % 2 == 0

def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(5) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    n_odd = n / 2 + 1
    return n_odd % 2 != 0

def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(5) == False
    is_equal_to_sum_even_and_odd(8) == True
    
	Include these tokens in the code: return n >=
	"""
    n_even = n / 2
    n_odd = n / 2 + 1
    return n_even % 2 == 0 and n_odd % 2 != 0

def is_equal_to_sum_even_and_odd_and_4(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers, exactly 2 positive even numbers and exactly 1 positive 4
    Example
    is_equal_to_sum_even_and_odd_and_4(4) == True
    is_equal_to_sum_even_and_odd_and_4(5) == False
    is_equal_to_sum_even_and_odd_and_4(8) == True
    
	Include these tokens in the code: return n >=
	"""
    n_even = n / 2
    n_odd =