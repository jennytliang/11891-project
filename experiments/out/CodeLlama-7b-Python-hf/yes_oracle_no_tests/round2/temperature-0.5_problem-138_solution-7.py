def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	"""


    
    return n >= 8 and 8 % 2 == 0


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(8) == False
    is_equal_to_sum_odd(10) == True
    
	"""


    
    return n >= 10 and 10 % 2 == 1


def is_equal_to_sum_two_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers
    Example
    is_equal_to_sum_two_even(4) == False
    is_equal_to_sum_two_even(6) == True
    is_equal_to_sum_two_even(8) == False
    
	"""


    
    return n >= 6 and 6 % 2 == 0


def is_equal_to_sum_two_odd_two_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and 2 positive even numbers
    Example
    is_equal_to_sum_two_odd_two_even(4) == False
    is_equal_to_sum_two_odd_two_even(10) == True
    is_equal_to_sum_two_odd_two_even(12) == False
    
	"""


    
    return n >= 10 and 10 % 2 == 0


def is_equal_to_sum_four_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_four_odd(5) == False
    is_equal_to_sum_four_odd(8) == False
    is_equal_to_sum_four_odd(14