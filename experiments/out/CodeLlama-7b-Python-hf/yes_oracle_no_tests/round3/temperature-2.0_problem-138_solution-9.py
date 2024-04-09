def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8

print(is_equal_to_sum_even(8))

def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 6

print(is_equal_to_sum_odd(6))

def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and exactly 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(4) == True
    is_equal_to_sum_even_and_odd(6) == False
    is_equal_to_sum_even_and_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 4

print(is_equal_to_sum_even_and_odd(4))

def is_equal_to_sum_even_and_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_and_even(4) == False
    is_equal_to_sum_even_and_even(6) == True
    is_equal_to_sum_even_and_even(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 6

print(is_equal_to_sum_even_and_even(6))

def is_equal_to_sum_odd_and_odd(n):
    """Evaluate whether the given number n can