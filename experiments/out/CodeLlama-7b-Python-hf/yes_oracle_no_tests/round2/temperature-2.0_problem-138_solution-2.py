def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: and n % 2 == 0
	"""

    return n % 2 == 0


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(7) == True
    is_equal_to_sum_odd(21) == True
    
    Include these tokens in the code: and n % 2 == 1
    """

    return n % 2 == 1


def is_equal_to_sum_even_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers
    and 2 positive odd numbers
    Example
    is_equal_to_sum_even_odd(4) == False
    is_equal_to_sum_even_odd(6) == False
    is_equal_to_sum_even_odd(8) == False
    is_equal_to_sum_even_odd(10) == True
    is_equal_to_sum_even_odd(14) == True
    
    Include these tokens in the code: and n % 2 == 0 and n % 2 == 1
    """

    return n % 2 == 0 and n % 2 == 1


def is_equal_to_sum_odd_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers
    and 2 positive odd numbers
    Example
    is_equal_to_sum_odd_odd(5) == False
    is_equal_to_sum_odd_odd(7) == False
    is_equal_to_sum_odd_odd(11) == True
    is_equal_to_sum_odd_odd(13) == True
    
    Include these tokens in the code: and n % 2 == 1 and n % 2 == 1
    """

    return n % 2 == 1 and n % 