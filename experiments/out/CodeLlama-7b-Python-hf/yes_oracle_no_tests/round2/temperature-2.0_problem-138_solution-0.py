def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _
	"""

    return n % 2 == 0 and n == sum(range(1, n + 1, 2))


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_odd(9) == True
    is_equal_to_sum_odd(7) == True
    is_equal_to_sum_odd(8) == False
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _
	"""

    return n % 2 != 0 and n == sum(range(1, n + 1, 2))


def is_equal_to_sum_even_and_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers and exactly 2 positive even numbers
    Example
    is_equal_to_sum_even_and_odd(2) == False
    is_equal_to_sum_even_and_odd(10) == True
    is_equal_to_sum_even_and_odd(14) == False
    
	Include these tokens in the code: and
	Do not include these tokens in the code: def is _ equal _ to _
	"""

    return n == sum(range(1, n + 1, 2)) and n == sum(range(1, n + 1, 2))


def is_equal_to_sum_even_and_odd_and_three(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers, exactly 2 positive even numbers and exactly 1 positive number
    Example
    is_equal_to_sum_even_and_odd_and_three(5) == True
    is_equal_to_sum_even_and_odd_and_three(6) == False
    is_equal_to_sum_even_and_odd_and_three(9) == True
