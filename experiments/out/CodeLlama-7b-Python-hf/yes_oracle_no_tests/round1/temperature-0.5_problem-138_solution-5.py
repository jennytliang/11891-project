def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=  8 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 8 and (n % 4 == 0)



def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(7) == True
    is_equal_to_sum_odd(11) == False
    
	Include these tokens in the code: return n >=  5 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 5 and (n % 2 == 1)



def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(10) == True
    is_equal_to_sum_even_and_odd(20) == False
    
	Include these tokens in the code: return n >=  10 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 10 and (n % 2 == 0)



def is_equal_to_sum_two_numbers(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive numbers
    Example
    is_equal_to_sum_two_numbers(4) == True
    is_equal_to_sum_two_numbers(8) == True
    is_equal_to_sum_two_numbers(10) == True
    is_equal_to_sum_two_numbers(12) == False
    
	Include these tokens in the code: return n >=  8 and
	Do not include these tokens in the code: if
	"""

    
    return n >= 8 and (n %