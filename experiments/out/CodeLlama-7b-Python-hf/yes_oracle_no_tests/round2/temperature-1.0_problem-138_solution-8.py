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
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: and n % 2 != 0
	"""

    return n % 2 != 0


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(6) == True
    is_equal_to_sum_even_and_odd(8) == False
    is_equal_to_sum_even_and_odd(10) == True
    is_equal_to_sum_even_and_odd(12) == False
    
	Include these tokens in the code: and n % 2 != 0
	"""

    return n % 2 != 0


def is_equal_to_sum_even_and_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 1 positive even number, 1 positive odd number and 2 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd_and_three(4) == False
    is_equal_to_sum_even_and_odd_and_three(6) == False
    is_equal_to_sum_even_and_odd_and_three(8) == True
    is_equal_to_sum_even_and_odd_and_three(10) == False
    is_equal_to_sum_even_and_odd_and_three(