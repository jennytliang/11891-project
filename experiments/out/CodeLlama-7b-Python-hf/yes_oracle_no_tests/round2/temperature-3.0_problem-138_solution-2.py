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
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(8) == True
    
	Include these tokens in the code: and n % 2 == 1
	"""

    return n % 2 == 1


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(4) == False
    is_equal_to_sum_even_and_odd(5) == False
    is_equal_to_sum_even_and_odd(10) == True
    
	Include these tokens in the code: and n % 2 == 0
	"""

    return n % 2 == 0


def is_equal_to_sum_even_and_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and exactly 2 positive even numbers and exactly 1 positive integer
    Example
    is_equal_to_sum_even_and_odd_and_three(4) == False
    is_equal_to_sum_even_and_odd_and_three(5) == False
    is_equal_to_sum_even_and_odd_and_three(10) == True
    
	Include these tokens in the code: and n % 2 == 0
	"""

    return n % 2 == 0


def is_equal_to_sum_even_and_odd_and_two(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and