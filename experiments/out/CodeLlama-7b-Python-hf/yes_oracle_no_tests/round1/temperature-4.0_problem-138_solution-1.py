def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""

    if n % 2 == 0:
        return n >= 8
    else:
        return n >= 4


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(4) == False
    is_equal_to_sum_odd(6) == False
    is_equal_to_sum_odd(8) == True
    
	Include these tokens in the code: return n >=
	"""

    if n % 2 == 0:
        return n >= 4
    else:
        return n >= 8


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers and exactly 4 positive odd numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(6) == False
    is_equal_to_sum_even_and_odd(8) == False
    is_equal_to_sum_even_and_odd(10) == True
    
	Include these tokens in the code: return n >=
	"""

    if n % 2 == 0:
        return n >= 10
    else:
        return n >= 6


def is_equal_to_sum_even_and_odd_and_3(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers, exactly 4 positive odd numbers and exactly 1 positive number of 3
    Example
    is_equal_to_sum_even_and_odd_and_3(4) == False
    is_equal_to_sum_even_and_odd_and_3(6) == False
    is_equal_to_sum_even_and_odd_and_3(8) == False
    is_equal_to_sum