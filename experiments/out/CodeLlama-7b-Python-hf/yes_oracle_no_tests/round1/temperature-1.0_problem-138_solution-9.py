def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8 #TODO: implement this method

def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(9) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 9 #TODO: implement this method

def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(10) == True
    is_equal_to_sum_even_and_odd(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 10 #TODO: implement this method

def is_equal_to_sum_even_and_odd_and_3(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number, 1 positive odd number and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd_and_3(12) == True
    is_equal_to_sum_even_and_odd_and_3(8) == False
    
	Include these tokens in the code: return n >=
	"""
    return n >= 12 #TODO: implement this method

def is_equal_to_sum_even_and_odd_and_4(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number, 1 positive odd number and 3 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd_and_4(16) == True
    is_equal_to_sum_even_and_odd_and_4(8) == False