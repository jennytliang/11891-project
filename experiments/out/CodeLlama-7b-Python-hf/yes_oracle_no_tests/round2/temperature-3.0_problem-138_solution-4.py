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
    is_equal_to_sum_odd(8) == True
    is_equal_to_sum_odd(12) == True
    
	Include these tokens in the code: and n % 2 == 1
	"""

    return n % 2 == 1


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(8) == True
    is_equal_to_sum_even_and_odd(12) == True
    
	Include these tokens in the code: and n % 2 == 1 and n % 2 == 0
	"""

    return n % 2 == 1 and n % 2 == 0


def is_equal_to_sum_two_even_and_two_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and exactly 2 positive even numbers
    Example
    is_equal_to_sum_two_even_and_two_odd(4) == False
    is_equal_to_sum_two_even_and_two_odd(8) == True
    is_equal_to_sum_two_even_and_two_odd(12) == True
    
	Include these tokens in the code: and n % 2 == 1 and n % 2 == 0
	"""

    return n % 2 == 1 and n % 2 == 0


def is_equal_to_sum_four_multiples_of_four(n