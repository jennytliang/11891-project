def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 8

#print(is_equal_to_sum_even(4))
#print(is_equal_to_sum_even(6))
#print(is_equal_to_sum_even(8))


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(9) == False
    is_equal_to_sum_odd(11) == False
    is_equal_to_sum_odd(12) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 12

#print(is_equal_to_sum_odd(9))
#print(is_equal_to_sum_odd(11))
#print(is_equal_to_sum_odd(12))


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_odd(12) == False
    is_equal_to_sum_even_odd(14) == False
    is_equal_to_sum_even_odd(16) == True
    
	Include these tokens in the code: return n >=
	"""
    return n >= 16

#print(is_equal_to_sum_even_odd(12))
#print(is_equal_to_sum_even_odd(14))
#print(is_equal_to_sum_even_odd(16))


def is_equal_to_sum_even_odd_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number, 1 positive odd number, and 2 positive even numbers
    Example
    is_equal_to_sum_even_odd_even(12) == False
   