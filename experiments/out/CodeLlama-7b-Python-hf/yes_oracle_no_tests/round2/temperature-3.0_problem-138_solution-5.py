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
    is_equal_to_sum_odd(9) == False
    is_equal_to_sum_odd(11) == False
    is_equal_to_sum_odd(12) == True
    
	Include these tokens in the code: and n % 2 == 1
	"""

    return n % 2 == 1


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers and 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(10) == False
    is_equal_to_sum_even_and_odd(12) == True
    is_equal_to_sum_even_and_odd(14) == False
    
	Include these tokens in the code: and n % 2 == 0 and n % 2 == 1
	"""

    return n % 2 == 0 and n % 2 == 1


def is_equal_to_sum_even_and_odd_and_three_times_five(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers and 1 positive even number and 3 times 5
    Example
    is_equal_to_sum_even_and_odd_and_three_times_five(15) == False
    is_equal_to_sum_even_and_odd_and_three_times_five(17) == False
    is_equal_to_sum_even_and_odd_and_three_times_five(20) == True
    is_equal_to_sum_even_and_odd_and_three_times_five(25) == False
    
	Include these tokens in the code: and n % 2 == 